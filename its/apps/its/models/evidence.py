# -*- coding: utf-8 -*-

__all__ = [
    'Evidence',
    'UserEvidence'
]

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Evidence(models.Model):
    
    code = models.CharField(
        _('Código'),
        max_length=50
    )

    name = models.CharField(
        _('Nome'),
        max_length=50
    )

    def __str__(self):
        return f'{self.name}'


class UserEvidence(models.Model):

    evidence = models.ForeignKey(
        Evidence,
        on_delete=models.CASCADE,
        related_name='users'
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