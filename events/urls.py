"""
@author: Przemyslaw Bieganski, bieg4n@gmail.com
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # /mainMap/
    url(r'^mainMap/', views.main_map, name='mainMap'),
    # /events/
    url(r'^listOfEvents/', views.list_of_events, name='listOfEvents'),
    # details/<category>/<value>
    url(r'^details/(?P<category>[A-z]+)/(?P<value>[\w|\W]+)$',
        views.details_view, name='detailsView'),
    # /about/
    url(r'^about/', views.about, name='about'),
]
