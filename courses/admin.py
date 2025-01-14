from django.contrib import admin
from .models import Topic, Course, Lecture, Enroll

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_title', 'topic_slug', 'topic_is_active')
    list_editable = ('topic_slug', 'topic_is_active')
    list_filter = ('topic_is_active', 'topic_created_at')
    list_per_page = 10
    search_fields = ('topic_title', 'topic_description')
    prepopulated_fields = {"topic_slug": ("topic_title", )}


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_slug', 'course_is_active')
    list_editable = ('course_slug', 'course_is_active')
    list_filter = ('course_is_active', 'course_created_at')
    list_per_page = 10
    search_fields = ('course_title', 'course_description')
    prepopulated_fields = {"course_slug": ("course_title", )}


class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_title', 'course', 'lecture_slug', 'lecture_previewable')
    list_editable = ('lecture_slug', 'lecture_previewable')
    list_filter = ('lecture_previewable', 'lecture_created_at')
    list_per_page = 10
    search_fields = ('lecture_title', 'lecture_description')
    prepopulated_fields = {"lecture_slug": ("lecture_title", )}


class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_date')
    list_filter = ('user', 'course', 'enrolled_date')
    list_per_page = 10
    search_fields = ('user', 'course', 'enrolled_date')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Enroll, EnrollAdmin)

