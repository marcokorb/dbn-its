# -*- coding: utf-8 -*-

__all__ = []

from django.contrib import admin
from .models import (
    Subject,
    UserSubject,
    UserQuestionHistory,
    Question,
    Alternative,
    Evidence,
    Difficulty,
    QuestionEvidence,
    UserEvidence
)


class AlternativeAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class SubjectAdmin(admin.ModelAdmin):
    pass


class UserQuestionHistoryAdmin(admin.ModelAdmin):
    pass


class UserSubjectAdmin(admin.ModelAdmin):
    pass


class EvidenceAdmin(admin.ModelAdmin):
    pass


class SimpleEvidenceAdmin(admin.ModelAdmin):
    pass


class ObservableEvidenceAdmin(admin.ModelAdmin):
    pass


class DifficultyAdmin(admin.ModelAdmin):
    pass


class QuestionEvidenceAdmin(admin.ModelAdmin):
    pass


class UserEvidenceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Alternative, AlternativeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(UserQuestionHistory, UserQuestionHistoryAdmin)
admin.site.register(UserSubject, UserSubjectAdmin)
admin.site.register(Evidence, EvidenceAdmin)
admin.site.register(Difficulty, DifficultyAdmin)
admin.site.register(QuestionEvidence, QuestionEvidenceAdmin)
admin.site.register(UserEvidence, UserEvidenceAdmin)