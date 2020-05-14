# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: D:\Project\3year_2term\project\Fei4ki\student_helper_backend\user_app\admin.py
# Compiled at: 2020-05-09 03:05:38
# Size of source mod 2**32: 1235 bytes
from django.contrib import admin
import django.contrib.auth.admin as BaseUserAdmin
from .models import Teacher, User, Comment, Student, Department

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('last_name', 'first_name', 'is_staff', 'is_active')
    list_filter = ('last_name', 'first_name', 'is_staff', 'is_active')
    fieldsets = (
     (
      None, {'fields': (('first_name', 'last_name'), 'username', 'password', 'email', 'student')}),
     (
      'Permissions', {'fields': ('is_staff', 'is_active')}))
    add_fieldsets = (
     (
      None,
      {'classes':('wide', ), 
       'fields':(('first_name', 'last_name'), 'username', 'password1', 'password2', 'email', 'student',
 'is_staff', 'is_active')}),)
    search_fields = ('last_name', )
    ordering = ('last_name', )


admin.site.register(User, UserAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'rating')
    fields = [('first_name', 'last_name'), 'rating', 'department']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(Comment)
admin.site.register(Department)
# okay decompiling admin.cpython-37.pyc
