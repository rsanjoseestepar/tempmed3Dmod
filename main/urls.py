
from django.conf.urls import url
from main import views
from django.contrib.auth import *

from django.conf.urls import patterns, url, include
from django.contrib import admin
from main import views
from django.conf.urls.static import static
from med3Dmodel import settings
from django import forms
from main import forms
from django.contrib.auth import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register2/$', views.register2 , name='register2'),
    url(r'^upload/$', views.upload , name='upload'),
    url(r'^upload_medimg/$', views.upload_medimg, name='upload_medimg'),
	url(r'^upload_model/$', views.upload_model, name='upload_model'),
	url(r'^upload_form/$', views.upload_form, name='upload_form'),
	url(r'^navigation/$', views.navigation, name='navigation'),
	url(r'^files/$', views.files, name='files'),
	url(r'^(?P<id>\d+)/$', views.viewer, name='viewer'),
	url(r'^vm(?P<id>\d+)/$', views.viewermod, name='viewermod'),
	url(r'^delete(?P<id>\d+)/$', views.delete, name='delete'),
	url(r'^deletemodel(?P<id>\d+)/$', views.deletemodel, name='deletemodel'),
	url(r'^generate/(?P<id>\d+)/$', views.generate, name='generate'),
	url(r'^browser(?P<id>\d+)/$', views.browser, name='browser'),
	url(r'^converter(?P<id>\d+)/$', views.converter, name='converter'),
	url(r'^settings(?P<id>\d+)/$', views.settings, name='settings'),
	url(r'^order/$', views.order, name='order'),
	url(r'^roi/$', views.roi , name='roi'),
	url(r'^comp/$', views.comp , name='comp'),
	url(r'^comptwo/$', views.comptwo , name='comptwo'),
	url(r'^compfour/$', views.compfour , name='compfour'),

]
