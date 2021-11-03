from django.shortcuts import render
from catalogo.models import Book

# from django.http import HttpResponse


# Create your views here.

def indice(request):
    '''
    Página inicial de nuestra Web
    '''
    libros = Book.objects.all()

    datos = {'autor': 'Víctor Navarro', 'libros' : libros}

    return render(request, 'index.html', context=datos)