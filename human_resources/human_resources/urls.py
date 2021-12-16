"""human_resources URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidate/', include('candidates.urls')),
]
