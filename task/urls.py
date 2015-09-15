

from django.conf.urls import url
from main import views
from django.contrib.auth import *

from django.conf.urls import patterns, url, include
from django.contrib import admin
from task import views
from django.conf.urls.static import static
from med3Dmodel import settings
from django import forms
from main import forms
from django.contrib.auth import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^nhdr2nrrd/$', views.nhdr2nrrd, name='nhdr2nrrd'),


]
