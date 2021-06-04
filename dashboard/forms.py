from django import forms
from .models import Meme


class PostMeme(forms.ModelForm):
    class Meta():
        model = Meme
        fields = ['name', 'caption', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }