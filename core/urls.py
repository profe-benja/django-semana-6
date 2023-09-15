from django.urls import path
from .views import inicio_sesion, logout, index, contacto, categorias, registro, categorias_idioma, libro_show, libro_index, libro_create, libro_delete

urlpatterns = [
    path('login', inicio_sesion, name='login'),
    path('logout', logout, name='logout'),
    
    
    
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
    
    
    
    # path('usuarios/', views.usuario_list, name='usuario_list'),
    # path('usuarios/create/', views.usuario_create, name='usuario_create'),
    # path('usuario/<int:pk>/', views.usuario_update, name='usuario_update'),
    # path('usuario/<int:pk>/delete', views.usuario_delete, name='usuario_delete'),

]
