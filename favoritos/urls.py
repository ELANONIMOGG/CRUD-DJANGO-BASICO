from django.urls import path
from .views import *


app_name = 'favoritos'

urlpatterns = [
    path('', index_favoritos, name='index'), # 127.0.0.1:8000
    path('crear', crear_favoritos, name='crear'),
    path('borrar/<int:pk>', borrar_favortios, name='borrar'),
    path('detalle/<int:pk>', detalle_favorito, name='detalle'),
    path('actualizar/<int:pk>', actualizar_favoritos, name='actualizar'),


]
