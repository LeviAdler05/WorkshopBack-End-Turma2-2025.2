"""
URL configuration for meuprojeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from primeiro_app import views as primeiro_views  # primeiro_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeiro_views.pagina_inicial, name='pagina_inicial'),  # página inicial do projeto
    path('primeiro/', include('primeiro_app.urls')),
    path('app2/', include('app2.urls')),  # agora o app2 cuida das próprias rotas
    path('core/', include('dia4.core.urls')),


]
