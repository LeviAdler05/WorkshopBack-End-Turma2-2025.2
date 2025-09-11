from rest_framework import serializers
from .models import CatImage, CatImageError

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = ['id', 'image_url', 'created_at']

class CatImageErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImageError
        fields = ['id', 'error_message', 'timestamp']