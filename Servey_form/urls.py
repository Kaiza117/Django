from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Servey_form/result', views.result),
]