from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + ' - ' + str(self.id)
    
class Libro(models.Model):
    codigo_isbn = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.nombre
    
    
# añadimos el usuario profile
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)
    
    def __str__(self):
        return self.user.username + ' - ' + self.role
    