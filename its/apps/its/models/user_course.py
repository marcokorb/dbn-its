# -*- coding: utf-8 -*-

__all__ = [
    'UserCourse',
    'UserCourseEvidence',
    'UserCourseQuestion'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .course import (
    Course,
    CourseQuestion
)
from .evidence import Evidence
from .network import Network
from .question import Question


class UserCourse(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    completed = models.BooleanField(
        _('Completo'),
        default=False
    )


class UserCourseEvidence(models.Model):

    course = models.ForeignKey(
        Evidence,
        on_delete=models.CASCADE,
        related_name='user_evidences'
    )

    evidence = models.ForeignKey(
        Evidence,
        on_delete=models.CASCADE,
        related_name='user_courses'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses_evidences'
    )

    time_slice = models.IntegerField(
        _('Expansão no Tempo'),
        default=0
    )

    observations = models.CharField(
        _('Observações'),
        default='',
        max_length=255
    )

    def __str__(self):
        return f'{self.user.username} - {self.evidence.name}' # pylint: disable=maybe-no-member



class UserCourseQuestion(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='users_questions'
    )

    network = models.ForeignKey(
        Network,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_courses_questions'
    )

    question = models.ForeignKey(
        CourseQuestion,
        on_delete=models.CASCADE,
        related_name='users_courses'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses_questions'
    )

    status = models.BooleanField(
        _('Status'),
        default=True
    )
