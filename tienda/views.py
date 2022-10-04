from django.shortcuts import render

from.models import Producto, Categoria

# Create your views here.
def index(request):
    lista_productos = Producto.objects.all()
    lista_categorias = Categoria.objects.all()
    context = {
        'productos':lista_productos,
        'categorias':lista_categorias
    }
    return render(request,'index.html', context)