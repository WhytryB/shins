from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from .views import *

urlpatterns = [
    path('',MainView.as_view(), name='main'),
    path('download', download, name='download'),
    path('down_sog', download_sog, name='down_sog')
]