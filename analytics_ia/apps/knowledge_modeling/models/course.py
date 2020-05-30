# -*- coding: utf-8 -*-

__all__ = [
    'Course',
    'CourseQuestion',
    'UserCourse'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .question import Question


class Course(models.Model):

    name = models.CharField(
        _('Nome'),
        max_length=255
    )


class CourseQuestion(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='courses'
    )


class UserCourse(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses'
    )
