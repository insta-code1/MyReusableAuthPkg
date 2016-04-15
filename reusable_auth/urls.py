from django.conf.url import urllib
from views import *

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='logout'),
    url(r'^logoutr/$', logout, name='logout'),
    url(r'^profile/$', profile, name='profile'),
]