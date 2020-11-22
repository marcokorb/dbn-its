# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import (
    Alternative,
    Course,
    CourseQuestion,
    Question,
    UserSubject,
    UserEvidence,
    UserCourse,
    UserCourseQuestion
)
from .serializers import (
    CourseSerializer,
    QuestionSerializer,
    UserSerializer,
    CourseQuestionSerializer,
)


@api_view(['POST'])
def login(request):

    user, _ = User.objects.get_or_create(username=request.data['username'])

    courses = Course.objects.all() # pylint: disable=maybe-no-member

    for course in courses:

        UserCourse.objects.get_or_create(course=course, user=user) # pylint: disable=maybe-no-member

    serializer = UserSerializer(user)

    return Response(serializer.data)


@api_view(['GET'])
def courses(request):

    courses = Course.objects.all() # pylint: disable=maybe-no-member

    serializer = CourseSerializer(
        courses,
        many=True,
        read_only=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def user_question(request):

    course = Course.objects.get(id=request.query_params['course_id']) # pylint: disable=maybe-no-member
    user = User.objects.get(username=request.query_params['username']) # pylint: disable=maybe-no-member

    user_course = UserCourse.objects.get(course=course, user=user) # pylint: disable=maybe-no-member

    if user_course.completed:
        pass

    if not UserCourseQuestion.objects.filter(course=course, user=user).exists(): # pylint: disable=maybe-no-member

        course_question = CourseQuestion.objects.filter(course=course).order_by('number').first() # pylint: disable=maybe-no-member

    else:

        last_user_question = UserCourseQuestion.objects.filter(course=course, user=user).latest('pk') # pylint: disable=maybe-no-member

        course_question = CourseQuestion.objects.filter(course=course, number__gt=last_user_question.question.number).order_by('number').first() # pylint: disable=maybe-no-member

    return Response(CourseQuestionSerializer(course_question).data)


@api_view(['POST'])
def user_answer(request):

    from IPython import embed; embed()

    alternative_id = request.data['alternativeId']
    question_id = request.data['questionId']

    alternative = Alternative.objects.get(id=alternative_id) # pylint: disable=maybe-no-member
    course = Course.objects.get(id=request.query_params['course_id']) # pylint: disable=maybe-no-member
    question = Question.objects.get(id=question_id) # pylint: disable=maybe-no-member
    user = User.objects.get(username=request.query_params['username']) # pylint: disable=maybe-no-member

    course_question = CourseQuestion.objects.get(course=course, question=question) # pylint: disable=maybe-no-member

    user_course_question, _ = UserCourseQuestion.objects.get_or_create( # pylint: disable=maybe-no-member
        course_question=course_question,
        network=course.network,
        user=user
    )

    user_course_question.status = alternative.status
    user_course_question.save()

    #Todo: Calculate probabilities
