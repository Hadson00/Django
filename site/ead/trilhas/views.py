from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def variavel(request):
    form = SiteForm
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    x = Site.objects.all()

    return render(request, 'var.html',{'users':x, 'form':form})