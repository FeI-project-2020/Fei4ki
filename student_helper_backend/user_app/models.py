from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # For User use default features

    # For Student
    # If User have student_num that in not equal to Null, then it is Student

    student = models.OneToOneField( 'Student', 
                                    on_delete=models.SET_NULL,
                                    null=True, 
                                    blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Student(models.Model):
    student_num = models.IntegerField(unique=True)
    course      = models.IntegerField()
    group       = models.CharField(max_length=10)
    captain     = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student_num}'


class Teacher(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20) 
    rating      = models.IntegerField()


class Comment(models.Model):
    commentator = models.ForeignKey('User', 
                                    on_delete=models.SET_NULL,
                                    null=True, 
                                    blank=True)
    comment = models.TextField(max_length=1000, help_text="Your comment")
    time    = models.TimeField(auto_now=True)