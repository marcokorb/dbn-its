# -*- coding: utf-8 -*-

__all__ = ['Question']

from django.db import models
from django.utils.translation import gettext_lazy as _

from .node import Node


class Question(models.Model):

    description = models.CharField(
        _('Descrição'),
        default='',
        max_length=255
    )

    content = models.TextField(
        _('Conteúdo'),
        max_length=255
    )

    evidences = models.ManyToManyField(Node, blank=True)

    def __str__(self):

        evidences_as_text =  ', '.join([e.name for e in self.evidences.all()]) # pylint: disable=maybe-no-member

        return f'{self.description} - ({evidences_as_text})'
