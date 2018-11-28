from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='home'),
    url(r'^QT1/', views.SearchMatchupFromTeam, name='SearchMatchupFromTeam'),
    url(r'^QT2/', views.SearchPlayersFromTeam, name='SearchPlayersFromTeam'),
    url(r'^QT3/$', views.QT3.as_view(), name='QueryType3'),
    url(r'^QT4/$', views.QT3.as_view(), name='QueryType4'),
]
