from django.contrib import admin
from django.urls import path, include
from orderfood.views import *

urlpatterns = [
    path('order', order, name='order'),
    path('logout', logout_user, name='logout'),
    path('report', report, name='report'),
    path('register', RegisterUser.as_view(), name='register'),
    path('auth', LoginUser.as_view(), name='auth'),
    path('', index, name='index')
]
