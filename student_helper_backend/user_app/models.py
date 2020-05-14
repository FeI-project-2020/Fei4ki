# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: D:\Project\3year_2term\project\Fei4ki\student_helper_backend\user_app\models.py
# Compiled at: 2020-05-09 03:04:13
# Size of source mod 2**32: 1852 bytes
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    student = models.OneToOneField('Student', on_delete=(models.SET_NULL),
      null=True,
      blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Student(models.Model):
    student_num = models.IntegerField(unique=True)
    course = models.IntegerField()
    group = models.CharField(max_length=10)
    captain = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.student_num}")


class Department(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.OneToOneField('Department', on_delete=(models.SET_NULL), null=True, blank=True)
    rating = models.IntegerField()


class Comment(models.Model):
    commentator = models.ForeignKey('User', on_delete=(models.SET_NULL),
      null=True,
      blank=True,
      related_name='comments')
    text = models.TextField(max_length=1000, help_text='Your comment')
    time = models.TimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=(models.SET_NULL),
      blank=True,
      null=True,
      related_name='children')
# okay decompiling models.cpython-37.pyc
