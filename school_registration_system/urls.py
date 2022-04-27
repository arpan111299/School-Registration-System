from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('schoolApp.urls')),
    path('api/',include('school_api.urls')),
]
