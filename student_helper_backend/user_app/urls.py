from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views
urlpatterns = [
 path('rest/users', views.UserListView.as_view()),
 path('rest/user/create/', views.UserCreateView.as_view()),
 path('rest/user/<int:pk>/', views.UserView.as_view()),

 path('rest/student/<int:pk>/', views.StudentView.as_view()),

 path('rest/comments', views.CommentListView.as_view()),
 path('rest/comment/create/', views.CommentCreateView.as_view()),
 path('rest/comment/<int:pk>/', views.CommentView.as_view()),

 path('rest/teachers', views.TeacherListView.as_view()),
 path('rest/teacher/create/', views.TeacherCreateView.as_view()),
 path('rest/teacher/<int:pk>/', views.TeacherView.as_view()),

 path('rest/departments', views.DepartmentListView.as_view()),
 path('rest/department/create/', views.DepartmentCreateView.as_view()),
 path('rest/department/<int:pk>/', views.DepartmentView.as_view())]
