from rest_framework import serializers
import sys
from .models import User, Comment, Student, Teacher, Department

class StudentSerializer(serializers.ModelSerializer):
    """Student info"""

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        """Create and return a new student."""
        student = (Student.objects.create)(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.student_num = validated_data.get('student_num', instance.student_num)
        instance.course = validated_data.get('course', instance.course)
        instance.group = validated_data.get('username', instance.group)
        instance.captain = validated_data.get('captain', instance.captain)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    """Get/Post comment"""
    commentator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class FilterReviewListSerializer(serializers.ListSerializer):
    """Filter for comments, return comments only with parent = None"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=(self.context))
        return serializer.data


class CommentListSerializer(serializers.ModelSerializer):
    """List of comments"""
    children = RecursiveSerializer(many=True)
    commentator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'commentator', 'text', 'time', 'children')
        list_serializer_class = FilterReviewListSerializer


class UserSerializer(serializers.ModelSerializer):
    """User info"""
    student = StudentSerializer()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'student',
                  'last_login')

    def create(self, validated_data):
        """Create and return a new user."""
        student_data = validated_data.pop('student')
        student = (Student.objects.create)(**student_data)
        user = (User.objects.create)(student=student, **validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'student' in validated_data:
            student_data = validated_data.pop('student')
            print(student_data, file=(sys.stderr))
            if instance.student == None:
                instance.student = (Student.objects.create)(**student_data)
            else:
                instance.student.student_num = student_data.get('student_num', instance.student.student_num)
                instance.student.course = student_data.get('course', instance.student.course)
                instance.student.group = student_data.get('group', instance.student.group)
                instance.student.captain = student_data.get('captain', instance.student.captain)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    """List of users"""
    student = StudentSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']


class TeacherSerializer(serializers.ModelSerializer):
    """Get/Post comment"""

    class Meta:
        model = Teacher
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """Get/Post comment"""

    class Meta:
        model = Department
        fields = '__all__'
