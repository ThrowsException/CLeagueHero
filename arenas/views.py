from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import detail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
from django.utils.decorators import method_decorator
from django.template import RequestContext, loader
from social.backends.utils import load_backends
from django.conf import settings
from social.apps.django_app.utils import psa

from arenas.models import Arena
from arenas.decorators import render_to
from .forms import RatingForm
from .models import Rating


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
        r = Arena.objects.order_by('title')
        return r


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Arena
    template_name = 'arenas/detail.html'

    def get_context_data(self, **kwargs):
        print kwargs
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = RatingForm
        return context


class RatingView(LoginRequiredMixin, detail.SingleObjectMixin, generic.FormView):
    model = Arena
    template_name = 'arenas/detail.html'
    form_class = RatingForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        rating = RatingForm(request.POST)
        print request.POST
        if rating.is_valid():
            r = Rating()
            r.ice_surface = request.POST['ice_surface']
            r.referees = request.POST['referees']
            r.lockers = request.POST['lockers']
            r.league = request.POST['league']
            r.teams = request.POST['teams']
            r.comment = request.POST['comment']
            r.arena = self.object
            r.user = request.user

            r.save()
        return super(RatingView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        print "great success"
        return reverse('arenas:detail', kwargs={'pk': self.object.pk})


def home(request):
    c = context()
    if request.GET.get('next'):
        c = context(next=request.GET['next'])

    return render_to_response('arenas/home.html',
                              context_instance=RequestContext(request, c))


@login_required
@render_to('arenas/home.html')
def done(request):
    """Login complete view, displays user data"""
    # return render_to_response('arenas/home.html',
                             # context_instance=RequestContext(request, context()))
    return context()

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

def context(**extra):
    return dict({
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)
