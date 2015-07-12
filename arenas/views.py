from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
from django.utils.decorators import method_decorator
from django.template import RequestContext, loader
from social.backends.utils import load_backends
from django.conf import settings
from social.apps.django_app.utils import psa

from arenas.models import Arena


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'arenas/index.html'
    context_object_name = 'arena_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Arena.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Arena
    template_name = 'arenas/detail.html'


def home(request):
    return render_to_response('arenas/home.html',
                              context_instance=RequestContext(request, context()))


@login_required
def done(request):
    """Login complete view, displays user data"""
    return render_to_response('arenas/home.html',
                              context_instance=RequestContext(request, context()))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

def context(**extra):
    return dict({
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)
