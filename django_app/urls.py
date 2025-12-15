from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import socket

def health_check(request):
    return JsonResponse({
        "status": "healthy", 
        "pod_hostname": socket.gethostname()
    })

def home(request):
    return JsonResponse({
        "message": "Hello from Django Kubernetes App!",
        "pod_hostname": socket.gethostname()
    })

urlpatterns = [
    path('', home),
    path('health/', health_check),
    path('admin/', admin.site.urls),
]
