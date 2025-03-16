import requests
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('contacts', views.contacts, name = 'contacts'),
    path('chat', views.chat, name = 'chat'),
    path('settings', views.settings, name = 'settings'),
    path('pay', views.pay, name = 'pay'),
    path('entry', views.user_entry, name = 'user'),
    path('register', views.user_reg, name = 'reg'),
]
