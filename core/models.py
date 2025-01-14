from django.db import models
from django.contrib.auth.models import User

#  For Django Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, verbose_name="Short Description")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.user.username


# Django Signals to Create Profile Model
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    