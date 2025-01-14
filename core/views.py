from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'account/profile.html')
    else:
        messages.error(request, "Please login to access your profile.")
        return redirect('account_login')


def update_profile(request):
    return render(request, 'account/update_profile.html')


def save_profile(request):
    if request.method == "POST":
        # Check whether the user is logged in or not
        if request.user.is_authenticated:
            # Get updated Data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            date_of_birth = request.POST.get('date_of_birth')
            bio = request.POST.get('bio')
            address = request.POST.get('address')

            try:
                # Save Updated Data
                user = User.objects.get(id=request.user.id)
                user.first_name = first_name
                user.last_name = last_name
                user.profile.date_of_birth = date_of_birth
                user.profile.bio = bio
                user.profile.address = address
                user.save()

                messages.success(request, "Profile Updated!")
                return redirect(profile)

            except:
                messages.error(request, "Failed to Update Profile")
                return redirect(profile)

        else:
            messages.error(request, "Please login to access your profile.")
            return redirect('account_login')


        messages.success(request, "Profile Updated!")
        return redirect(profile)
    
    else:
        messages.error(request, "Please make changes from update profile form.")
        return redirect(update_profile)