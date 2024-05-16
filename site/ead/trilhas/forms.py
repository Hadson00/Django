from django import forms
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'
        labels = {
            'email': 'email1',
            'path': 'img'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: hadson@gmail.com'
                }
            ),
            'path': forms.ClearableFileInput()
        }