from urllib import request
from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'Druids/base.html')

def index(request):
    return render(request, 'Druids/index.html')

def carrito(request):
    return render(request, 'Druids/carrito.html')

def contacto(request):
    return render(request, 'Druids/contacto.html')
 
def historialCompra(request):
    return render(request, 'Druids/historialCompra.html')

def inventario(request):
    return render(request, 'Druids/inventario.html')

def listadoProductos(request):
    return render(request, 'Druids/listadoProductos.html')

def listaUsuarios(request):
    return render(request, 'Druids/listaUsuarios.html')

def pago(request):
    return render(request, 'Druids/pago.html')

def pagoexitoso(request):
    return render(request, 'Druids/pagoexitoso.html')

def pedidos(request):
    return render(request, 'Druids/pedidos.html')

def perfil(request):
    return render(request, 'Druids/perfil.html')

def producto(request):
    return render(request, 'Druids/producto.html')

def sobreNosotros(request):
    return render(request, 'Druids/sobreNosotros.html')
