from django.shortcuts import render
from .forms import *
from OSRSBytes import Hiscores

# Create your views here.

def index(request):
    if request.method == 'POST': #verificar se o form foi comitado
        form = UsernameForm(request.POST)
        if form.is_valid():
            
            data = Hiscores(form.cleaned_data['nick'])
            attack = data.skill('attack', 'level')
            strength = data.skill('strength', 'level')
            defense = data.skill('defense', 'level')
            ranged = data.skill('ranged', 'level')
            magic = data.skill('magic', 'level')
            print(attack,defense,strength,ranged,magic)
            form.save()
    else:
        form = UsernameForm()
        data = ()

    return render(request,'index.html', {'form': form, 'data': data, 'attack': attack, 'strength': strength, 'defense': defense, 'ranged': ranged, 'magic': magic, })
