# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
    Alternative,
    Course,
    CourseQuestion,
    UserEvidence,
    Network,
    NetworkSubject,
    Node,
    Question,    
    UserSubject,
    UserCourse,
    UserCourseEvidence,
    UserCourseQuestion
)


class AlternativeAdmin(admin.ModelAdmin):

    ordering = ('question__pk', 'number')


admin.site.register(Alternative, AlternativeAdmin)


class CourseAdmin(admin.ModelAdmin):

    ordering = ('pk',)


class CourseQuestionAdmin(admin.ModelAdmin):
    
    ordering = ('course__pk', 'number', )


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseQuestion, CourseQuestionAdmin)


class UserEvidenceAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserEvidence, UserEvidenceAdmin)


class NetworkAdmin(admin.ModelAdmin):
    
    ordering = ('pk',)


class NetworkSubjectAdmin(admin.ModelAdmin):
    
    ordering = ('network_id', 'subject__name')


admin.site.register(Network, NetworkAdmin)
admin.site.register(NetworkSubject, NetworkSubjectAdmin)


class QuestionAdmin(admin.ModelAdmin):

    ordering = ('description',)


admin.site.register(Question, QuestionAdmin)


class NodeAdmin(admin.ModelAdmin):

    ordering = ('is_evidence', 'name')


class UserSubjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Node, NodeAdmin)
admin.site.register(UserSubject, UserSubjectAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    pass


class UserCourseEvidenceAdmin(admin.ModelAdmin):
    pass


class UserCourseQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(UserCourseEvidence, UserCourseEvidenceAdmin)
admin.site.register(UserCourseQuestion, UserCourseQuestionAdmin)
