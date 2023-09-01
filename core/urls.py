from django.urls import path
from .views import categorias, registro, categorias_idioma, libro_ingles, libro_show

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('categorias', categorias, name="categorias"),
    path('registro', registro, name="registro"),
    path('categorias/idioma', categorias_idioma, name="categorias_idioma"),
    # path('libro/ingles', libro_ingles, name="libro_ingles")
    path('libro/<int:id>', libro_show, name="libro_show")
]
