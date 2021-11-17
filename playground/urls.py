from django.urls import path
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('check/', views.first_func)
]