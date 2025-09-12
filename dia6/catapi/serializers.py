from rest_framework import serializers
from .models import CatImage, CatImageError

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = "__all__"

class CatImageErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImageError
        fields = "__all__"
