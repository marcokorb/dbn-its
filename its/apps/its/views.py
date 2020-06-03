# -*- coding: utf-8 -*-

__all__ = ['inference_view']

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# from .bayesian_network import BayesianNetwork
from .models import (
    Alternative,
    Course,
    CourseQuestion,
    Question,
    Subject,
    UserSubject,
    Evidence,
    UserEvidence,
    UserCourse,
    UserCourseQuestion
)
from .serializers import (
    CourseSerializer,
    QuestionSerializer,
    UserSerializer
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

    return Response(QuestionSerializer(course_question.question).data)


@api_view(['POST'])
def user_answer(request):
    
    from IPython import embed; embed()

    alternative_id = request.data['alternativeId']
    question_id = request.data['questionId']

    alternative = Alternative.objects.get(id=alternative_id) # pylint: disable=maybe-no-member
    course = Course.objects.get(id=request.query_params['course_id']) # pylint: disable=maybe-no-member
    question = Question.objects.get(id=question_id) # pylint: disable=maybe-no-member
    user = User.objects.get(username=request.query_params['username']) # pylint: disable=maybe-no-member

    course_question = CourseQuestion.objects.get(course=course, question_id=question_id) # pylint: disable=maybe-no-member

    # {'alternativeId': '13', 'questionId': 3}

    # user = User.objects.get(username=request.query_params['username'])

    # with transaction.atomic():

    #     question = Question.objects.get(pk=request.data['questionId'])

    #     alternative = Alternative.objects.get(pk=request.data['alternativeId'])

    #     evidences = question.get_evidences(status=alternative.status)

    #     bayesian_network = BayesianNetwork()

    #     UserQuestionHistory.objects.create(
    #         question=question,
    #         user=user,
    #         status=alternative.status
    #     )

    #     print(evidences)

    #     for new_evidence, status in evidences.items():

    #         evidence = QuestionEvidence.objects.get(name=new_evidence)

    #         user_evidence, _ = UserEvidence.objects.get_or_create(
    #             user=user,
    #             evidence=evidence
    #         )

    #         user_evidence.status = status
    #         user_evidence.save()

    #         current_evidences = {}

    #         for predecessor in bayesian_network.get_predecessors(new_evidence):

    #             # Iteration through all successors of each predecessor
    #             for successor in bayesian_network.get_successors(predecessor):

    #                 if UserEvidence.objects.filter(evidence__name=successor, user=user).exists():

    #                     # Add to the evidence set
    #                     current_evidences.update({successor: int(UserEvidence.objects.get(evidence__name=successor, user=user).status)})

    #             print(current_evidences)

    #             if Subject.objects.filter(name=predecessor).exists():

    #                 subject = Subject.objects.get(name=predecessor)

    #                 updated_value = bayesian_network.query_evidence(
    #                     predecessor,
    #                     current_evidences
    #                 )

    #                 user_subject, _ = UserSubject.objects.get_or_create(
    #                     user=user,
    #                     subject=subject
    #                 )

    #                 user_subject.value = updated_value
    #                 user_subject.time_index += 1

    #                 user_subject.save()

    #             print(updated_value, predecessor, current_evidences)

    #             # Clear the evidence set for the next iteration
    #             current_evidences.clear()

    # return Response({
    #     'alternative_status': alternative.status,
    # })
