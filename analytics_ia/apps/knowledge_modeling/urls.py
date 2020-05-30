# -*- coding: utf-8 -*-

from django.urls import re_path

from . import views

app_name = 'knowledge_modeling'

urlpatterns = [
    re_path(
        r'^inference/$',
        views.inference_view,
        name='inference'
    ),
    re_path(
        r'^question/$',
        views.QuestionViewSet.as_view({'get': 'list'}),
        name='question'
    ),
    re_path(
        r'^user_answer/$',
        views.user_answer,
        name='user_answer'
    ),
    re_path(
        r'^user_question/$',
        views.user_question,
        name='user_question'
    )
]
