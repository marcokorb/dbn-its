"""ITS serializers module."""
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Alternative, Course, CourseQuestion, Question


class AlternativeSerializer(serializers.ModelSerializer):
    """Alternative serializer."""

    class Meta:
        model = Alternative
        fields = ("pk", "content", "number", "status")


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""

    alternatives = AlternativeSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("pk", "content", "alternatives")


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    class Meta:
        model = User
        fields = ("pk", "username")


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer."""

    class Meta:
        model = Course
        fields = ("pk", "name")


class CourseQuestionSerializer(serializers.ModelSerializer):
    """Course question serializer."""

    question = QuestionSerializer(read_only=True)

    class Meta:
        model = CourseQuestion
        fields = ("pk", "number", "question")
