from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    x = Curso.objects.all()
    return render(request, 'site/index.html',{'users': x})
    

def cadastro(request):
    form = CursoForm
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'site/cards.html',{'form': form})