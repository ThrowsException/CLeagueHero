from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from arenas.models import Arena


class IndexView(generic.ListView):
    template_name = 'arenas/index.html'
    context_object_name = 'arena_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Arena.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Arena
    template_name = 'arenas/detail.html'
