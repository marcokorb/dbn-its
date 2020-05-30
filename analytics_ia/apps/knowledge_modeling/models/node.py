# -*- coding: utf-8 -*-

__all__ = [
    'Node'
]

from django.db import models
from django.utils.translation import gettext_lazy as _

from .network import Network


class Node(models.Model):

    class Meta:
        abstract = True

    code = models.CharField(
        _('Código'),
        max_length=50
    )

    name = models.CharField(
        _('Nome'),
        max_length=50
    )

    network = models.ForeignKey(
        Network,
        on_delete=models.CASCADE,
        related_name='nodes'
    )

    children = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return f'{self.name}({self.pk})'
