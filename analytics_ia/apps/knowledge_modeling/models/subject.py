# -*- coding: utf-8 -*-

__all__ = [
    'Subject',
    'UserSubject'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .node import Node


class Subject(Node):
    pass


class UserSubject(models.Model):

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    def __str__(self):
        return f'{self.user.username} - {self.subject.name}(T: {self.time_index})'


class UserSubjectTimeSlice(models.Model):

    user_subject = models.ForeignKey(
        UserSubject,
        on_delete=models.CASCADE,
        related_name='time_slices'
    )

    time_slice = models.IntegerField(
        _('Índice de Tempo'),
        default=0
    )

    false_value = models.DecimalField(
        _('Probabilidade Falsa'),
        default=0,
        decimal_places=10,
        max_digits=10
    )

    true_value = models.DecimalField(
        _('Probabilidade Verdadeira'),
        default=0,
        decimal_places=10,
        max_digits=10
    )
