from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main_info(request):
    return render(request, 'main info.html')

def experience(request):
    return render(request, "experience.html")

def education(request):
    return render(request, "education.html")