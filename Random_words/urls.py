from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Random_words/generate', views.generate),
    path('Random_words/reset', views.reset)
]