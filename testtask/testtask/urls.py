from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

import orderfood.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orderfood.urls')),
]
