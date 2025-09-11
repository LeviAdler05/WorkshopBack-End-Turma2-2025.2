from rest_framework import viewsets
from .models import CatImage, CatImageError
from .serializers import CatImageSerializer, CatImageErrorSerializer
import requests

class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all()
    serializer_class = CatImageSerializer

def perform_create(self, serializer):
    import requests
    try:
        response = requests.get("https://cataas.com/cat?json=true", verify=False)
        if response.status_code == 200:
            image_path = response.json().get('url', '')
            full_url = f"https://cataas.com{image_path}"
            serializer.save(image_url=full_url)
        else:
            CatImageError.objects.create(error_message=f"Erro HTTP: {response.status_code}")
            serializer.save(image_url="")
    except Exception as e:
        CatImageError.objects.create(error_message=str(e))
        serializer.save(image_url="")

class CatImageErrorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatImageError.objects.all().order_by('-timestamp')
    serializer_class = CatImageErrorSerializer