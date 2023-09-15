from django.contrib import admin

from .models import Categoria, Libro, UserProfile

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(UserProfile)
