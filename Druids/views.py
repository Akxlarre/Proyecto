from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from Druids.models import Producto
from .forms import ContactoForm, RegistroProductoForm, EditarProductoForm

# Create your views here.

def base(request):
    return render(request, 'Druids/base.html')

def index(request):
    return render(request, 'Druids/index.html')

def carrito(request):
    return render(request, 'Druids/carrito.html')
 
def historialCompra(request):
    return render(request, 'Druids/historialCompra.html')

def inventario(request):
    Productos = Producto.objects.all()
    form_registrar = RegistroProductoForm()

    if request.method == "POST":
        form_registrar = RegistroProductoForm(data=request.POST, files=request.FILES)
        if form_registrar.is_valid():
            form_registrar.save()
            return redirect(to='inventario')

    context = {
        'Productos': Productos,
        'formularioRegistrarProducto': form_registrar,
    }
    return render(request, 'Druids/inventario.html', context)

def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form_editar = EditarProductoForm(instance=producto)

    if request.method == "POST":
        form_editar = EditarProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form_editar.is_valid():
            form_editar.save()
            return redirect(to='inventario')

    context = {
        'formularioEditarProducto': form_editar,
        'producto': producto,
    }
    return render(request, 'Druids/editarProducto.html', context)

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from Druids.models import Producto

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        producto.delete()
        return redirect('inventario')
    
    context = {
        'producto': producto
    }
    return render(request, 'Druids/eliminar_producto.html', context)

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

def Contacto(request):

    form = ContactoForm()

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            return redirect('contacto')  # Redirige a la página de contacto
    else:
        form = ContactoForm()
    return render(request, 'Druids/contacto.html', {'formularioContacto': form})
