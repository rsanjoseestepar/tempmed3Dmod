from django.conf.urls import include, url
from worker import views
from django.contrib import admin

urlpatterns = [
    url(r'^worker/', views.worker, name='worker'),
]