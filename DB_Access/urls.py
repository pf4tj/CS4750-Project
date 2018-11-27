from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^QT1/$', views.QT1.as_view(), name='QueryType1'),
    url(r'^QT2/$', views.QT2.as_view(), name='QueryType2'),
    url(r'^QT3/$', views.QT3.as_view(), name='QueryType3'),
    url(r'^QT4/$', views.QT4.as_view(), name='QueryType4'),
]
