from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'arenas.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'arenas.views.home'),
    url(r'^logout/$', 'arenas.views.logout'),
    url(r'^done/$', 'arenas.views.done', name='done'),
    url(r'^arenas/', include('arenas.urls', namespace="arenas")),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
