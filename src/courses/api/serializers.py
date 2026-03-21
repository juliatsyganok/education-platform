from rest_framework import serializers
from models import Course, Lesson, Enrollment, UserProfile

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'name', 'content', 'order']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'date_enrolled']
        read_only_fields = ['user', 'date_enrolled']