from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views

# URLConf
urlpatterns = [
    path('check/', views.first_func),
]