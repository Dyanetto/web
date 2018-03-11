#from django.contrib import admin
#from django.urls import path, include 
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.new, name='new'),
    url(r'^login/$', views.test, name='test'),
    url(r'^signup/$', views.test, name='test'),
    url(r'^question/(?P<index>\d+)/$', views.question, name='test'),
    url(r'^ask/$', views.test, name='test'),
    url(r'^popular/$', views.popular, name='test'),
    url(r'^new/$', views.test, name='test'),
]
