from django.conf.urls import patterns, url

from arenas import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$',
                           views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/rate/$', views.RatingView.as_view(), name='rate')
                       )
