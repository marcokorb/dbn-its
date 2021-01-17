# -*- coding: utf-8 -*-
from typing import List

from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import (
    Alternative,
    Course,
    CourseQuestion,
    Evidence,
    Question,
    UserSubject,
    UserEvidence,
    UserCourse,
    UserCourseEvidence,
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

        course_question = CourseQuestion.objects.filter(course=course, number__gt=last_user_question.course_question.number).order_by('number').first() # pylint: disable=maybe-no-member

    return Response(CourseQuestionSerializer(course_question).data)


@api_view(['POST'])
def user_answer(request):

    from IPython import embed; embed()

    # Extract alternative and question ids from request
    alternative_id: str = request.data['alternativeId']
    question_id: int = request.data['questionId']

    # Retrieve objects from the database
    alternative: Alternative = Alternative.objects.get(id=alternative_id, question_id=question_id) # pylint: disable=maybe-no-member
    course: Course = Course.objects.get(id=request.query_params['course_id']) # pylint: disable=maybe-no-member
    question: Question = Question.objects.get(id=question_id) # pylint: disable=maybe-no-member
    user: User = User.objects.get(username=request.query_params['username']) # pylint: disable=maybe-no-member
    course_question: CourseQuestion = CourseQuestion.objects.get(course=course, question=question) # pylint: disable=maybe-no-member

    # for course_question in course.questions.filter():

    #     question = course_question.question

    #     if question.id == question_id:

    #         user_course_question, _ = UserCourseQuestion.objects.get_or_create( # pylint: disable=maybe-no-member
    #             course_question=course_question,
    #             network=course.network,
    #             user=user,
    #         )

    #         user_course_question.status = alternative.status
    #         user_course_question.save()

    #         for evidence in question.evidences.filter():

    #             UserCourseEvidence.objects.get_or_create(
    #                 course=course,
    #             )

    # I need to:
    #   - save the course question
    #   - increase the user course evidences.

    # Retrieve evidences related to the question
    question_evidences: List[int] = question.evidences.values_list('pk', flat=True).distinct()

    # Retrieve user course question
    user_course_question, _ = UserCourseQuestion.objects.get_or_create( # pylint: disable=maybe-no-member
        course=course,
        course_question=course_question,
        network=course.network,
        user=user
    )

    # Update user course question with the selected alternative status
    user_course_question.status = alternative.status
    user_course_question.save()

    # List to store course evidences
    course_evidences: List[Evidence] = []

    # Todo: I need to find a better way to extract the course evidences. This is not good.
    for course_question in course.questions.filter():

        evidences = course_question.question.evidences.all()

        course_evidences += evidences

    course_evidences = set(course_evidences)

    for evidence in course_evidences:

        user_course_evidence, _ = UserCourseEvidence.objects.get_or_create(
            course=course,
            evidence=evidence,
            user=user,            
        )

        user_course_evidence.time_slice += 1
        observation = int(alternative.status) if evidence.pk in question_evidences else ' ' 
        user_course_evidence.observations += f'{observation}'

        user_course_evidence.save()

    # Todo: Calculate probabilities using the UserCourseEvidence objects

    return Response({
        "alternative_status": alternative.status
    })

    #Todo: Calculate probabilities
