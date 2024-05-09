from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def lista(request):
    list = ['Hadson',
            'Raphael',
            'Rogerio',
            'Kamylle'
            ]
    for i in list:
        i += 1
        return(render(request,'index.html'))