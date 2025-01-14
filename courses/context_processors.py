from .models import Topic, Course, Enroll


def head_menu(request):
    topics = Topic.objects.filter(topic_is_active='Yes')
    context = {
        'topics': topics
    }
    return context


def my_courses(request):
    if request.user.is_authenticated:
        enrolled_courses = Enroll.objects.filter(user=request.user).order_by('-enrolled_date')[:5]
    else:
        enrolled_courses = None 
    context = {
        'enrolled_courses': enrolled_courses,
    }
    return context
