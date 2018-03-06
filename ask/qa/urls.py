from django.urls import re_path
from ask.views import *

urlpatterns = patterns('ask.views',
    re_path(r'^$', test, name='root'),
    re_path(r'^login/$', test, name='login'),
    re_path(r'^signup/$', test, name='singup'),
    re_path(r'^question/(?P<id>\d+)/$', test, name='question'),
    re_path(r'^ask/$', test, name='ask'),
    re_path(r'^popular/$', test, name='popular'),
    re_path(r'^new/$', test, name='new'),
    re_path(r'^', not_found, name='not_found'),
)
