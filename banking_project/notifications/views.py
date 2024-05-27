from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification

def index(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/index.html', {'notifications': notifications})

# Add other views as needed
