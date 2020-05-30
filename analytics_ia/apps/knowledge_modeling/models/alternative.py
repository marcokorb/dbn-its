# -*- coding: utf-8 -*-

__all__ = ['Alternative']


from django.db import models
from django.utils.translation import gettext_lazy as _
from .question import Question


class Alternative(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='alternatives'
    )

    content = models.TextField(
        _('Conteúdo'),
        max_length=50
    )

    number = models.CharField(
        _('Número'),
        max_length=5,
        null=True
    )

    status = models.BooleanField(
        _('Status'),
        default=False
    )

    def __str__(self):
        return f'{self.number} - {self.content}'
