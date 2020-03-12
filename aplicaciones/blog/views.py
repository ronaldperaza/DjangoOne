from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)            
        ).distinct()        

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})

def detallePost(request, slug):
    # post = Post.objects.get(
    #     slug = slug
    # )
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'post.html', {'detalle_post': post})

def generales(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria= Categoria.objects.get(nombre__iexact = "General")
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo_icontains = queryset) |
            Q(descripcion_icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General'), #nombre__iexact no importa mayusculas
        ).disinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales.html', {'posts': posts})

def programacion(request):

    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria= Categoria.objects.get(nombre__iexact = "Programacion")
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo_icontains = queryset) |
            Q(descripcion_icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion'), #nombre__iexact no importa mayusculas
        ).disinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programacion.html', {'posts': posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria= Categoria.objects.get(nombre__iexact = "Tecnologia")
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo_icontains = queryset) |
            Q(descripcion_icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'), #nombre__iexact no importa mayusculas
        ).disinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html', {'posts': posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria= Categoria.objects.get(nombre__iexact = "Video Juegos")
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo_icontains = queryset) |
            Q(descripcion_icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Video Juegos'), #nombre__iexact no importa mayusculas
        ).disinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'posts': posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria= Categoria.objects.get(nombre__iexact = "Tutoriales")
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo_icontains = queryset) |
            Q(descripcion_icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'), #nombre__iexact no importa mayusculas
        ).disinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tutoriales.html', {'posts': posts})

# def contacto(request):
#     return render(request, 'contacto.html')


