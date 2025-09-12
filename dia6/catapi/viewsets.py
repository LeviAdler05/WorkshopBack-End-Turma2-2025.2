import certifi
import requests
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import CatImage
from .serializers import CatImageSerializer

class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all()
    serializer_class = CatImageSerializer

    @action(detail=False, methods=["get"])
    def random(self, request):
        """Retorna uma imagem aleatória da The Cat API"""
        try:
            response = requests.get(
                "https://api.thecatapi.com/v1/images/search",
                verify=certifi.where()  # ← garante que o Requests encontre os certificados
            )
            response.raise_for_status()
            data = response.json()
            if not data:
                return Response({"error": "Nenhuma imagem encontrada"}, status=404)
            return Response({"url": data[0]["url"]})
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Erro ao buscar imagem: {str(e)}"}, status=500)
