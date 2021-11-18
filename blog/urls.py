from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views

# URLConf
app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('main_info/', views.main_info, name='main_info'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
]