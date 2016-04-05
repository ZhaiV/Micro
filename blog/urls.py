from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'index/',views.index),
    url(r'auth/',views.auth),
    url(r'register/',views.register),
    url(r'signup/',views.signup),
    url(r'welcome/',views.welcome),

]


