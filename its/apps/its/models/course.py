# -*- coding: utf-8 -*-

__all__ = [
    'Course',
    'CourseQuestion'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .network import Network
from .question import Question


class Course(models.Model):

    name = models.CharField(
        _('Nome'),
        max_length=255
    )

    network = models.ForeignKey(
        Network,
        blank=True,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return f'{self.pk} - {self.name}'


class CourseQuestion(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='courses'
    )


    number = models.IntegerField(
        _('Número'),
        default=1
    )

    def __str__(self):
        return f'{self.course.name} - {self.number} - {self.question}'
