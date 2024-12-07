from django.shortcuts import render, redirect
from .models import Topic, Course, Lecture, Enroll
from django.contrib import messages
from django.contrib.auth.decorators import login_required # for Access Control



# Create your views here.

def index(request):
    courses = Course.objects.filter(course_is_active='Yes', course_is_featured="Yes")
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)


def courses(request):
    courses = Course.objects.filter(course_is_active='Yes')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses.html', context)


def topic_courses(request, topic_slug):
    topic = Topic.objects.get(topic_slug=topic_slug)
    courses = Course.objects.filter(course_is_active='Yes', course_topic=topic)
    context = {
        'courses': courses,
        'topic': topic,
    }
    return render(request, 'courses/topic_courses.html', context)


def search_courses(request):
    if request.method == "GET":
        keyword = request.GET.get('q')
        courses = Course.objects.filter(course_is_active='Yes')
        searched_courses = courses.filter(course_title__icontains=keyword) | courses.filter(course_description__icontains=keyword)
        
        context = {
            'courses': searched_courses,
            'keyword': keyword,
        }
        return render(request, 'courses/search_courses.html', context)


def course_detail(request, course_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)

        # Check
        if request.user.is_authenticated:
            enrolled = Enroll.objects.filter(course=course, user=request.user)
        else:
            enrolled = None
        

        context = {
            'course': course,
            'lectures': lectures,
            'enrolled': enrolled,
        }
        return render(request, 'courses/course_detail.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


@login_required(login_url='account_login')
def lecture(request, course_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)
        first_lecture = Lecture.objects.filter(course=course.id)[:1]
        #Check User Enrolled
        enrolled = Enroll.objects.filter(course=course, user=request.user)

        context = {
            'course': course,
            'lectures': lectures,
            'first_lecture': first_lecture,
            'enrolled': enrolled,
        }
        # return render(request, 'courses/lecture.html', context)
        #Check User Enrolled
        if enrolled:
            return render(request, 'courses/lecture.html', context)
        else:
            #User Logged In but Not Enrolled
            messages.error(request, "Enroll Now to access this course.")
            return render(request, 'courses/course_detail.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


@login_required(login_url='account_login')
def lecture_selected(request, course_slug, lecture_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)
        lecture_selected = Lecture.objects.get(lecture_slug=lecture_slug)
        #Check User Enrolled
        enrolled = Enroll.objects.filter(course=course, user=request.user)

        context = {
            'course': course,
            'lectures': lectures,
            'lecture_selected': lecture_selected,
            'enrolled': enrolled,
        }
        # return render(request, 'courses/lecture_selected.html', context)
        #Check User Enrolled
        if enrolled:
            return render(request, 'courses/lecture_selected.html', context)
        else:
            #User Logged In but Not Enrolled
            messages.error(request, "Enroll Now to access this course.")
            return render(request, 'courses/course_detail.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


@login_required(login_url='account_login')
def enroll(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)

    try:
        Enroll.objects.create(user=user, course=course)
        messages.success(request, "Successfully enrolled to the Course.")
        return redirect(index)

    except:
        messages.error(request, "Couldn't Enroll to the course. Please try again later.")
        return redirect(index)


@login_required(login_url='account_login')
def enrolled_courses(request):

    try:
        courses = Enroll.objects.filter(user=request.user)
        context = {
            'courses': courses,
        }
        return render(request, 'courses/enrolled_courses.html', context)

    except:
        messages.error(request, "Couldn't Enroll to the course. Please try again later.")
        return redirect(index)
    

        

