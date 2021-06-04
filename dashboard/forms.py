from django import forms
from .models import Meme


class PostMeme(forms.ModelForm):
    class Meta():
        model = Meme
        fields = ['name', 'caption', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }