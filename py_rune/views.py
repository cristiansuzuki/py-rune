from django.shortcuts import render
from .forms import *
from OSRSBytes import Hiscores

# Create your views here.

def index(request):
    if request.method == 'POST': #verificar se o form foi comitado
        form = UsernameForm(request.POST)
        if form.is_valid():
            data = Hiscores(form.cleaned_data['nick'])
            if data.status==200:
                attack = data.skill('attack', 'level')
                strength = data.skill('strength', 'level')
                defense = data.skill('defense', 'level')
                ranged = data.skill('ranged', 'level')
                magic = data.skill('magic', 'level')
            else:
                attack = ('Usuario nao encontrado')
                strength = ('Usuario nao encontrado')
                defense = ('Usuario nao encontrado')
                ranged = ('Usuario nao encontrado')
                magic = ('Usuario nao encontrado')

    else:       
        form = UsernameForm()
        data = ()

    return render(request,'index.html', {'form': form, 'data': data, 'attack': attack, 'strength': strength, 'defense': defense, 'ranged': ranged, 'magic': magic, })
