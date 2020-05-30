# -*- coding: utf-8 -*-

__all__ = [
    'Question',
    'UserQuestionHistory'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .subject import Subject


class Question(models.Model):

    number = models.IntegerField(
        _('Número'),
        default=1
    )

    content = models.TextField(
        _('Conteúdo'),
        max_length=255
    )

    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'({self.pk}){self.number} - {self.content}'

    def get_evidences(self, status):

        return {
            evidence.name: status
            for evidence in self.evidences.filter()
        }


class UserQuestionHistory(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='user_questions_history'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='question_history'
    )

    status = models.BooleanField(
        _('Status'),
        default=True
    )
