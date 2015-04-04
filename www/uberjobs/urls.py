from django.conf.urls import patterns, url

from uberjobs import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^series/$', views.serieslist, name='serieslist'),
        url(r'^series/(?P<series_id>[a-zA-Z0-9]+)/$', views.seriesdetail, name='seriesdetail'),
        url(r'^serieschart/(?P<series_id>[a-zA-Z0-9]+)/$', views.serieschart, name='serieschart'),
        url(r'^serieschartcompare/(?P<series_id>[a-zA-Z0-9]+)/$', views.serieschartcompare, name='serieschartcompare'),
        url(r'^serieschartscatter/(?P<series_id>[a-zA-Z0-9]+)/$', views.serieschartscatter, name='serieschartscatter'),
        url(r'^model/(?P<series_id>[a-zA-Z0-9]+)/$', views.seriesmodel, name='seriesmodel'),
    )