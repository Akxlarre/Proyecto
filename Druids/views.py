from urllib import request
from django.shortcuts import render, redirect
from .forms import ContactoForm, RegistroProductoForm

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

def registrarContacto(request):

    form = ContactoForm()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            return redirect('contacto')  # Redirige a la página de contacto
    else:
        form = ContactoForm()
    return render(request, 'Druids/registrarContacto', {'formularioContacto': form})

def registroProducto(request):

    form = RegistroProductoForm()

    if request.method == 'POST':
        form = RegistroProductoForm(data=request.POST ,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='inventario')
    else:
        form = RegistroProductoForm()
    
    data = {'form': form}
    return render(request, 'Druids/inventario.html', data)
