from django.http import JsonResponse
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    data = [
        {
            'codigo': producto.codigo,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio)
        }
        for producto in productos
    ]
    return JsonResponse(data, safe=False)