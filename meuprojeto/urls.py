from django.contrib import admin
from django.urls import path, include
from primeiro_app import views as primeiro_views  # primeiro_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeiro_views.pagina_inicial, name='pagina_inicial'),  # página inicial do projeto
    path('primeiro/', include('primeiro_app.urls')),
    path('app2/', include('app2.urls')),  # agora o app2 cuida das próprias rotas
    path('core/', include('dia4.core.urls')),
    path('viacep/', include('dia5.viacep.urls'))


]
