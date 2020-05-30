# -*- coding: utf-8 -*-

__all__ = [
    'Network'
]

from django.db import models
from django.utils.translation import gettext_lazy as _


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
        return f'{self.name}({self.pk})'
