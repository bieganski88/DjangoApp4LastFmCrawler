from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # /mainMap/
    url(r'^mainMap/', views.mainMap, name='mainMap'),
    # /events/
    url(r'^listOfEvents/', views.listOfEvents, name='listOfEvents'),
    # details/<category>/<value>
    url(r'^details/(?P<category>[A-z]+)/(?P<value>[\w|\W]+)$', views.detailsView, name='detailsView'),
    # /about/
    url(r'^about/', views.about, name='about'),
]