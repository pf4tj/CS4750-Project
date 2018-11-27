from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^scheduler/$', views.SchedulerPageView.as_view(), name='scheduler'),
]
