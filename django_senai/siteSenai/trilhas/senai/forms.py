from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        labels = {
            'nomeCurso' : 'nome',
            'preco' : 'valor',
            'tempo' : 'duração',
            'path' : 'imagem'
        }
        widgets = {
            'nomeCurso': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Excel'
                }
            ),
            'preco': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 100.00'
                }
            ),
            'tempo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 50h'
                }
            ),
            'path': forms.ClearableFileInput(),
        }