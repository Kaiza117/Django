"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("time_display/", include("time_display.urls")),
    path("admin/", admin.site.urls),
    path("Random_words/", include("Random_words.urls")),
    path("Random_words/generate", include("Random_words.urls")),
    path("Random_words/reset", include("Random_words.urls")),
    path("Servey_form", include("Servey_form.urls")),
    path("Servey_form/result", include("Servey_form.urls")),
]
