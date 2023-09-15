from django.shortcuts import render, get_object_or_404, redirect

# añadio UserProfile
from .models import Libro, Categoria, UserProfile


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .decorators import role_required

from django.contrib.auth.models import User

from django.contrib import messages

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
# @login_required
@role_required('admin', 'cliente')
def libro_index(request):
    libros = Libro.objects.all() # SELECT * FROM libro
    
    perfil = request.session.get('perfil')
    contexto = {
        'libros': libros,
        'perfil': perfil
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

@role_required('admin')
def libro_create(request):
    
    categorias = Categoria.objects.all()
    
    contexto = {
        'categorias': categorias
    }
    
    return render(request, 'libro/create.html', contexto)

@role_required('admin','cliente')
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


# Semana 6
# AUTH

def inicio_sesion(request): 
    
    # messages.success(request, 'bienvendio a la pagina de inicio de sesion')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')
        # print('')
        # print('')
        # print(f"usuario {usuario} clave {clave}")
        # print(request.POST)
        # print('')
        # print('')
        
        user = authenticate(request, username=usuario, password=clave)
        # print('')
        # print('')
        # print(user)
        # print('')
        # print('')
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            
            request.session['perfil'] = profile.role
            
            
            login(request, user)
            
            return redirect('libro_index')
        else:
            context = {
                'error' : 'Error intente nuevamente.'
            }
            return render(request, 'auth/inicio_sesion.html', context)
        
    return render(request, 'auth/inicio_sesion.html')

@role_required('cliente','admin')
def logout_view(request):
    logout(request)
    return redirect('inicio_sesion')


# CRUD USUARIO

# @login_required
# def usuario_list(request):
#     usuarios = User.objects.all()
#     context = {'usuarios': usuarios}
#     return render(request, 'usuarios/index.html', context)

# @login_required
def usuario_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        role = 'cliente'
        UserProfile.objects.create(user=user, role=role) 

        return redirect('usuario_list')
    return render(request, 'usuarios/create.html')

# @login_required
def usuario_update(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.username = request.POST.get('username')
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.save()

        # role = request.POST.get('role')
        # user_profile.role = role
        # user_profile.save() 

        return redirect('usuario_list')
    context = {'usuario': usuario}
    return render(request, 'usuarios/update.html', context)

# @login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    context = {'usuario': usuario}
    return render(request, 'usuarios/delete.html', context)