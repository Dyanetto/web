from django.conf.urls import url
from ask.views import test

urlpatterns = patterns('ask.views',
    url(r'^$', test, name='root'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='singup'),
    url(r'^question/(?P<id>\d+)/', test, name='question'),
    url(r'^ask/$', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^', not_found, name='not_found'),
)
