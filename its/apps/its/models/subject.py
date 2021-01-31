"""Subject models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    """Subject model."""

    code = models.CharField(_("Código"), max_length=50)

    name = models.CharField(_("Nome"), max_length=50)

    def __str__(self):

        return f"{self.pk} - {self.name}"


class UserSubject(models.Model):
    """UserSubject model."""

    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="users_subjects"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subjects"
    )

    time_slice = models.IntegerField(_("Índice de Tempo"), default=0)

    false_value = models.DecimalField(
        _("Probabilidade Falsa"), default=0, decimal_places=10, max_digits=10
    )

    true_value = models.DecimalField(
        _("Probabilidade Verdadeira"),
        default=0,
        decimal_places=10,
        max_digits=10,
    )

    def __str__(self):
        return f"{self.user.username} - {self.subject.name}(T: {self.time_slice})"  # pylint: disable=maybe-no-member
