from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import  Teacher, User, Comment, Student

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('last_name', 'first_name', 'is_staff', 'is_active',)
    list_filter = ('last_name', 'first_name', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': (('first_name', 'last_name'), 'username', 'password', 'email', 'student')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (('first_name', 'last_name'), 'username', 'password1', 'password2', 'email', 'student',
                        'is_staff', 'is_active')}
        ),
    )
    search_fields = ('last_name',)
    ordering = ('last_name',)

admin.site.register(User, UserAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'rating')
    fields = [('first_name', 'last_name'), 'rating']

admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Student)
admin.site.register(Comment)