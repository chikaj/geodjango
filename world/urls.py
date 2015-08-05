from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^states/$', views.states, name='States'),
    url(r'^api/testpoints$', views.updateGeoLocation, name='updateGeoLocation'),
]
