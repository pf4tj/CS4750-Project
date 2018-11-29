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
    url(r'^QT4/$', views.QT4, name='QueryType4'),
    url(r'^PlayersWithoutTeam/', views.PlayersWithoutTeam, name='PlayersWithoutTeam'),
    url(r'^NoTeam/$', views.NoTeam, name='NoTeam'),
    url(r'^AddPlayer/', views.AddPlayerToTeam, name='AddPlayerToTeam'),
    url(r'^RemovePlayer/', views.RemovePlayerFromTeam, name='RemovePlayerFromTeam'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
