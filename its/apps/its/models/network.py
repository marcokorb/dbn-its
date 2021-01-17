# -*- coding: utf-8 -*-

__all__ = [
    'Network'
]

from django.core.serializers.json import DjangoJSONEncoder
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
        related_name='networks_subjects'
    )

    network_subjects = models.ManyToManyField(
        Subject,
        blank=True,
        related_name='networks_subjects_parents'
    )

    evidences = models.ManyToManyField(
        Evidence,
        related_name='networks_subjects_evidences'
    )

    def __str__(self):
        return f'{self.pk} - {self.network.name} - {self.subject.name}' # pylint: disable=maybe-no-member


class NetworkSubjectProbabilities(models.Model):

    network_subject = models.ForeignKey(
        NetworkSubject,
        on_delete=models.CASCADE,
        related_name='probabilities'
    )

    # Todo: This model is unnecessary and should be replaced 
    #  in the future because it does not really make sense.
    #  For, we will use it as experiment to have a simple way 
    #  to store the probabilities.

    # 'subjects_probabilities' contains the initial and transition values.
    subjects_probabilities = models.JSONField(
        blank=True, null=True, encoder=DjangoJSONEncoder
    )

    evidences_probabilities = models.JSONField(
        blank=True, null=True, encoder=DjangoJSONEncoder
    )

    def __str__(self):
        return f'{self.network_subject} - Probabilities' # pylint: disable=maybe-no-member
