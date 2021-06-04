from rest_framework import serializers
from dashboard.models import Meme
from django import forms

class MemeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Meme
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_uri(photo_url)