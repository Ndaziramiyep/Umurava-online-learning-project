from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('courses/', views.courses, name="courses"),
    path('courses/search/', views.search_courses, name="search-courses"),
    path('courses/enrolled-courses/', views.enrolled_courses, name="enrolled-courses"),

    path('courses/<slug:topic_slug>/', views.topic_courses, name="topic-courses"),
    path('course/<slug:course_slug>/', views.course_detail, name="course-detail"),
    path('course/<slug:course_slug>/lecture/', views.lecture, name="lecture"),
    path('course/<slug:course_slug>/lecture/<slug:lecture_slug>/', views.lecture_selected, name="lecture-selected"),

    path('course/enroll/<int:course_id>/', views.enroll, name="enroll"),
    
]
