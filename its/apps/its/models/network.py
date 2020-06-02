# -*- coding: utf-8 -*-

__all__ = [
    'Network'
]

from django.db import models
from django.utils.translation import gettext_lazy as _

from .evidence import Evidence
from .subject import Subject


class Network(models.Model):

    code = models.CharField(
        _('Código'),
        max_length=50
    )

    name = models.CharField(
        _('Nome'),
        max_length=50
    )

    def __str__(self):
        return f'{self.pk} - {self.name}'


class NetworkSubject(models.Model):

    network = models.ForeignKey(
        Network,
        on_delete=models.CASCADE,
        related_name='subjects'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='networks'
    )

    evidences = models.ManyToManyField(Evidence)

    def __str__(self):
        return f'{self.pk} - {self.network.name} - {self.subject.name}' # pylint: disable=maybe-no-member
