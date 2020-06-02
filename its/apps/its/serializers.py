# -*- coding: utf-8 -*-

__all__ = [
    'AlternativeSerializer',
    'CourseSerializer',
    'QuestionSerializer'
]

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Alternative,
    Course,
    Question
)


class AlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternative
        fields = ('pk', 'content', 'number', 'status')


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('pk', 'name')


class QuestionSerializer(serializers.ModelSerializer):

    alternatives = AlternativeSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'content', 'alternatives')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username')
