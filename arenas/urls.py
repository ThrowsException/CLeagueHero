from django.conf.urls import patterns, url

from arenas import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$',
                           views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/rate/$', views.RatingView.as_view(), name='rate'),
                       url(r'^(?P<pk>\d+)/add_player/$', 'arenas.views.add_player', name='add_player'),
                       url(r'^(?P<pk>\d+)/freeagents/$', 'arenas.views.freeagents', name='freeagents'),
                       )
