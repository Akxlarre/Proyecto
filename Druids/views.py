from urllib import request
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactoForm

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

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            return redirect('contacto')  # Redirige a una página de éxito
    else:
        form = ContactoForm()
    return render(request, 'Druids/contacto.html', {'formularioContacto': form})
