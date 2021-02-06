from rest_framework import serializers
from dashboard.models import Meme
from django import forms

class MemeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Meme
        fields = (
            'id', 'name', 'caption', 'url'
        )