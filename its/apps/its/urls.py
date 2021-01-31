"""Its urls module."""
from django.urls import re_path

from . import views

app_name = "its"

urlpatterns = [
    re_path(r"^login/$", views.login, name="login"),
    re_path(r"^courses/$", views.courses, name="courses"),
    re_path(r"^user_answer/$", views.user_answer, name="user_answer"),
    re_path(r"^questions/$", views.user_question, name="user_question"),
]
