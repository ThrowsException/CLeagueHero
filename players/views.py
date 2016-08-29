from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PlayerInfo
from .models import Positions


# Create your views here.
@login_required
def me(request):
    try:
        item = Positions.objects.get(customuser=request.user.id)
    except Positions.DoesNotExist:
        item = {'phone_number': ''}

    form = PlayerInfo(initial={'phone_number': item['phone_number']})
    return render(request, 'players/me.html', {'PlayerForm': form})

@login_required
def update_me(request):
    player = PlayerInfo(request.POST)

    player = Positions()
    player.position = request.POST['position']
    player.phone_number = request.POST['phone_number']
    try:
        player.save()
    except:
        return redirect(reverse('arenas:detail', kwargs={'pk': pk}))

    # return redirect(reverse('arenas:detail', kwargs={'pk': pk}))
    return render(request, 'players/me.html', {'PlayerForm': PlayerInfo})
