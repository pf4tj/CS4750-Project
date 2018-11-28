from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^QT1/', views.SearchMatchupFromTeam, name='SearchMatchupFromTeam'),
    url(r'^QT2/', views.SearchPlayersFromTeam, name='SearchPlayersFromTeam'),
    url(r'^QT3/', views.AddOrRemovePlayerFromTeam, name='AddOrRemovePlayerFromTeam'),
    url(r'^QT4/$', views.QT4.as_view(), name='QueryType4'),
    url(r'^PlayersWithoutTeam/', views.PlayersWithoutTeam, name='PlayersWithoutTeam'),
]
