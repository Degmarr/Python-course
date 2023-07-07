from django.urls import path
from . import views

urlspatterns = [
    path('', views.projects_index, name = "project_index"),
]
