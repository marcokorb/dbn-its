"""Admin models."""
from django import forms
from django.contrib import admin

from .models import (
    Alternative,
    Course,
    CourseQuestion,
    Evidence,
    Network,
    NetworkSubject,
    NetworkSubjectProbabilities,
    Question,
    Subject,
    UserCourse,
    UserCourseEvidence,
    UserCourseQuestion,
    UserEvidence,
    UserSubject,
)

# I need at least two tables:
# One for parent subjects and evidences?
# Other for transitions?


class AlternativeAdmin(admin.ModelAdmin):
    """Alternative admin model."""

    ordering = ("question__pk", "number")


admin.site.register(Alternative, AlternativeAdmin)


class CourseAdmin(admin.ModelAdmin):
    """Course admin model."""

    ordering = ("pk",)


class CourseQuestionAdmin(admin.ModelAdmin):
    """Course question admin model."""

    ordering = (
        "course__pk",
        "number",
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseQuestion, CourseQuestionAdmin)


class EvidenceAdmin(admin.ModelAdmin):
    """Evidence admin model."""

    ordering = ("name",)


class UserEvidenceAdmin(admin.ModelAdmin):
    """UserEvidence admin model."""

    pass


admin.site.register(Evidence, EvidenceAdmin)
admin.site.register(UserEvidence, UserEvidenceAdmin)


class NetworkAdmin(admin.ModelAdmin):
    """Network admin model."""

    ordering = ("pk",)


class NetworkSubjectAdmin(admin.ModelAdmin):
    """Network subject admin model."""

    ordering = ("network_id", "subject__name")


class NetworkSubjectProbabilitiesAdmin(admin.ModelAdmin):
    """Network subject probabilities admin model."""

    ordering = ("pk",)


admin.site.register(Network, NetworkAdmin)
admin.site.register(NetworkSubject, NetworkSubjectAdmin)
admin.site.register(
    NetworkSubjectProbabilities, NetworkSubjectProbabilitiesAdmin
)


class QuestionAdmin(admin.ModelAdmin):
    """Question admin model."""

    ordering = ("description",)


admin.site.register(Question, QuestionAdmin)


class SubjectAdmin(admin.ModelAdmin):
    """Subject admin model."""

    ordering = ("name",)


class UserSubjectAdmin(admin.ModelAdmin):
    """User subject admin model."""

    pass


admin.site.register(Subject, SubjectAdmin)
admin.site.register(UserSubject, UserSubjectAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    """UserCourse admin model."""

    pass


class UserCourseEvidenceAdmin(admin.ModelAdmin):
    """UserCourseEvidence admin model."""

    pass


class UserCourseQuestionAdmin(admin.ModelAdmin):
    """UserCourseQuestion admin model."""

    pass


admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(UserCourseEvidence, UserCourseEvidenceAdmin)
admin.site.register(UserCourseQuestion, UserCourseQuestionAdmin)
