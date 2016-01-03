from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^me/$', 'players.views.me', name='me')
                       )
