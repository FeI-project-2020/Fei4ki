from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .models import User, Student, Comment, Teacher, Department
from .serializers import UserListSerializer, UserSerializer, StudentSerializer, CommentSerializer, CommentListSerializer, TeacherSerializer, DepartmentSerializer

class UserView(APIView):
    """Get list of users """

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=(request.data), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_200_OK))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        result = user.delete()
        if result:
            return Response(status=(status.HTTP_200_OK))
        return Response(status=(status.HTTP_400_BAD_REQUEST))


class UserCreateView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_201_CREATED))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))


class UserListView(APIView):
    """Get list of users """

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class StudentView(APIView):
    """Student info"""

    def get(self, request, pk):
        student = Student.objects.get(student_num=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def patch(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=(request.data), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_200_OK))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        student = Student.objects.get(id=pk)
        result = student.delete()
        if result:
            return Response(status=(status.HTTP_200_OK))
        return Response(status=(status.HTTP_400_BAD_REQUEST))


class CommentView(APIView):

    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment, data=(request.data), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_200_OK))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        comment = Comment.objects.get(id=pk)
        result = comment.delete()
        if result:
            return Response(status=(status.HTTP_200_OK))
        return Response(status=(status.HTTP_400_BAD_REQUEST))


class CommentCreateView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_201_CREATED))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))


class CommentListView(APIView):
    """Get list of comments """

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)


class TeacherView(APIView):

    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def patch(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(teacher, data=(request.data), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_200_OK))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        result = teacher.delete()
        if result:
            return Response(status=(status.HTTP_200_OK))
        return Response(status=(status.HTTP_400_BAD_REQUEST))


class TeacherCreateView(APIView):

    def post(self, request):
        serializer = TeacherSerializer(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_201_CREATED))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))


class TeacherListView(APIView):
    """Get list of teachers """

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class DepartmentView(APIView):

    def get(self, request, pk):
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def patch(self, request, pk):
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(department, data=(request.data), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_200_OK))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        department = Department.objects.get(id=pk)
        result = department.delete()
        if result:
            return Response(status=(status.HTTP_200_OK))
        return Response(status=(status.HTTP_400_BAD_REQUEST))


class DepartmentCreateView(APIView):

    def post(self, request):
        serializer = DepartmentSerializer(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response((serializer.data), status=(status.HTTP_201_CREATED))
        return Response((serializer.errors), status=(status.HTTP_400_BAD_REQUEST))


class DepartmentListView(APIView):

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)
