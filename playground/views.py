from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser

def first_func(request):
    return render(request, 'test.html', {'name': 'Temirlan'})