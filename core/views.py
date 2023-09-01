from django.shortcuts import render

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

def libro_show(request, id):
    
    
    # [0,1,2]
    libros = ['ingles','matematica','fe']
    imagenes = ['img/libro-ingles.png','img/libro-matematicas.png','img/libro-fe.png']
    
    libro = libros[id-1]
    img = imagenes[id-1]
    
    contexto = {
        'nombre': libro,
        'img': img
    }
    return render(request, 'libro/show.html', contexto)