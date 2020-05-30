# -*- coding: utf-8 -*-

__all__ = [
    'Evidence',
    'UserEvidence'
]

from django.contrib.auth.models import User

from django.db import models
from django.utils.translation import gettext_lazy as _

from .question import Question

from .node import Node


class Evidence(Node):

    pass


class QuestionEvidence(models.Model):

    name = models.CharField(
        _('Nome'),
        max_length=50
    )

    evidence = models.ForeignKey(
        Evidence,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='evidences'
    )

    def __str__(self):
        return f'({self.pk}){self.name}'



class UserEvidence(models.Model):

    evidence = models.ForeignKey(
        QuestionEvidence,
        on_delete=models.CASCADE,
        related_name='users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='evidences'
    )

    time_expansion = models.CharField(
        _('Expansão no Tempo'),
        default=
        max_length=255
    )

    status = models.BooleanField(
        _('Status'),
        default=False
    )

    def __str__(self):
        return f'{self.user.username} - {self.evidence.name}'

