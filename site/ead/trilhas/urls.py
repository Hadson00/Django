from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('variavel/', views.variavel, name='exibir_variavel'),
    path('cadastro/', views.variavel, name='cadastro_variavel')
]