
import requests
from django.shortcuts import render

def catimages_home(request):
    image_url = None

    if request.method == "POST":
        try:
            response = requests.get("http://127.0.0.1:8000/api/catimages/random/")
            data = response.json()
            image_url = data.get("url")
        except Exception as e:
            print("Erro ao buscar imagem:", e)

    return render(request, "catimages.html", {"image_url": image_url})
