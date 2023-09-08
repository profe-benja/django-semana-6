from django.shortcuts import render, get_object_or_404, redirect

from .models import Libro, Categoria

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')


# Create your views here.
def categorias(request):
    return render(request, 'index.html')

def registro(request):
    
    # KEY: VALUE
    contexto = {
        'nombre': 'Benjamin 🪅🎊'
    }
    return render(request, 'registro.html', contexto)

def categorias_idioma(request):
    return render(request, 'categoria/idioma.html')
 
def libro_ingles(request):
    contexto = {
        'nombre': 'Ingles básico 1'
    }
    return render(request, 'libro/ingles.html', contexto)




# LIBROS

def libro_index(request):
    libros = Libro.objects.all() # SELECT * FROM libro
    
    contexto = {
        'libros': libros
    }
    
    
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        categoria_id = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        
        categoria = get_object_or_404(Categoria, id=categoria_id)
        
        print(f"nombre {nombre} categoria {categoria} descripcion {descripcion}")
        
        Libro.objects.create(
            codigo_isbn = codigo,
            nombre = nombre,
            descripcion = descripcion,
            categoria=categoria
        )
        # Libro.objects.create(
        #     codigo_isbn = codigo,
        #     nombre = nombre,
        #     descripcion = descripcion,
        #     categoria_id=categoria
        # )
    
    return render(request, 'libro/index.html', contexto)

def libro_create(request):
    
    categorias = Categoria.objects.all()
    
    contexto = {
        'categorias': categorias
    }
    
    return render(request, 'libro/create.html', contexto)


def libro_show(request, id):
    
    libro = get_object_or_404(Libro, id=id)
 
    contexto = {
        'libro': libro,
    }
    return render(request, 'libro/show.html', contexto)

def libro_delete(request, id):
    
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
 
    return redirect('libro_index')
    # return render(request, 'libro/index.html')



# def libro_show(request, id):
    
    
#     # [0,1,2]
#     libros = ['ingles','matematica','fe']
#     imagenes = ['img/libro-ingles.png','img/libro-matematicas.png','img/libro-fe.png']
    
#     libro = libros[id-1]
#     img = imagenes[id-1]
    
#     contexto = {
#         'nombre': libro,
#         'img': img
#     }
#     return render(request, 'libro/show.html', contexto)