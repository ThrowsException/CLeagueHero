from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PlayerInfo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def me(request):
    return render(request, 'players/me.html', {'PlayerForm': PlayerInfo})
