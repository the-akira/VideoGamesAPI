from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def documentation(request):
    return render(request, 'documentation.html')

def about(request):
    return render(request, 'about.html')