# -*- coding: utf-8 -*-

__all__ = [
    'Subject',
    'UserEvidence',
    'UserSubject'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Node(models.Model):

    code = models.CharField(
        _('Código'),
        max_length=50
    )

    name = models.CharField(
        _('Nome'),
        max_length=50
    )

    is_evidence = models.BooleanField(
      _('É uma evidência?'),
      default=False
    )

    def __str__(self):

        evidence_description = ' - Evidência' if self.is_evidence else ''

        return f'{self.pk} - {self.name} {evidence_description}'


class UserEvidence(models.Model):

    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='users_evidences'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='evidences'
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


class UserSubject(models.Model):

    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='users_subjects'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subjects'
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

    def __str__(self):
        return f'{self.user.username} - {self.subject.name}(T: {self.time_slice})' # pylint: disable=maybe-no-member
