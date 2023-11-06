from django.contrib import admin

from tutorial.models import Course, Lesson, Payment


@admin.register(Course)
class TutorialCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview')


@admin.register(Lesson)
class TutorialLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview', 'video_link', 'course')


@admin.register(Payment)
class TutorialPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'lesson', 'amount', 'payment_method')
