from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)
