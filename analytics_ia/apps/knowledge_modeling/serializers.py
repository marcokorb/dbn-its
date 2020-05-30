# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Question, Alternative


class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = ('pk', 'content', 'number', 'status')


class QuestionSerializer(serializers.ModelSerializer):

    alternatives = AlternativeSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'number', 'content', 'alternatives')
