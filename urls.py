from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("log_exercise", views.log_exercise, name="log_exercise"),
    path("history", views.history, name="history")
    # path("contacts", views.contacts, name="contacts"),
    # path("base", views.base, name="base"),
]
