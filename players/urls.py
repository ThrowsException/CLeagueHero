from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^me/$', 'players.views.me', name='me'),
                       url(r'^update_me/$', 'players.views.update_me', name='update_me')
                       )
