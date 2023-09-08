from django.urls import path
from .views import index, contacto, categorias, registro, categorias_idioma, libro_show, libro_index, libro_create, libro_delete

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', index, name="index"),
    path('contacto', contacto, name="contacto"),
    
    
    path('categorias', categorias, name="categorias"),
    path('registro', registro, name="registro"),
    path('categorias/idioma', categorias_idioma, name="categorias_idioma"),
    # path('libro/ingles', libro_ingles, name="libro_ingles")
   
    
    
    
    path('libros', libro_index, name="libro_index"),
    path('libros/create', libro_create, name="libro_create"),
    path('libros/<int:id>', libro_show, name="libro_show"),
    path('libros/<int:id>/delete', libro_delete, name="libro_delete"),
]
