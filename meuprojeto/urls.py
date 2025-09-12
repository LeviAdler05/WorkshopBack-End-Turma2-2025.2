# meuprojeto/urls.py
from django.contrib import admin
from django.urls import path, include
from primeiro_app import views as primeiro_views
from rest_framework.routers import DefaultRouter
from dia6.catapi.viewsets import CatImageViewSet  # Removido CatImageErrorViewSet
from dia6.catapi.views import catimages_home

# Configuração do router do DRF
router = DefaultRouter()
router.register(r'catimages', CatImageViewSet, basename='catimage')
# Removido CatImageErrorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeiro_views.pagina_inicial, name='pagina_inicial'),
    path('primeiro/', include('primeiro_app.urls')),
    path('app2/', include('app2.urls')),
    path('core/', include('dia4.core.urls')),
    path('viacep/', include('dia5.viacep.urls')),
    path('api/', include(router.urls)),

    # site HTML
    path("cats/", catimages_home, name="catimages_home"),
]
