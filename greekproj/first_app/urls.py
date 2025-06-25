from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
	path("", views.index, name="index"),
	path("nouns/", views.nouns, name="nouns"),
	path("verbs/", views.verbs, name="verbs"),
	path("adjectives/", views.adjectives, name="adjectives"),
	path("participles/", views.participles, name="participles"),
]