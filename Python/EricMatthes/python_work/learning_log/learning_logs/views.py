from django.shortcuts import render

# Create your views here.

def index(request):
    """Домашняя страница приложения learning_log"""
    return render(request, 'learning_logs/index.html')
