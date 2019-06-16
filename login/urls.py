from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login'), name='authapp-logout'),

]