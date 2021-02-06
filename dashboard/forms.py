from django import forms
from .models import Meme


class PostMeme(forms.ModelForm):
    class Meta():
        model = Meme
        fields = (
            'name', 'caption', 'url'
        )