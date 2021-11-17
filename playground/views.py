from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def first_func(request):
    return render(request, 'test.html', {'name': 'Temirlan'})