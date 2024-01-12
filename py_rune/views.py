from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    if request.method == 'POST': #verificar se o form foi comitado
        form = UsernameForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'index.html')
