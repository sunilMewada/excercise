from django.conf.urls import url
from django.contrib.admin import register

from . import views

app_name = 'polls'
urlpatterns = [
    url (r'^$', views.index, name='index'),
    url (r'^restricted/$', views.restricted, name='restricted'),
    url (r'^anonymous/$', views.anonymous, name='anonymous'),
]
