from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from Druids.models import CarritoItem, DetallePedido, Pedido, Producto, Usuario
from .forms import ContactoForm, LoginForm, PagoForm, RegistroAdminForm, RegistroProductoForm, EditarProductoForm , RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def base(request):
    return render(request, 'Druids/base.html')

def index(request):
    return render(request, 'Druids/index.html')

def carrito(request):
    carrito_items = CarritoItem.objects.all()
    total = sum(item.total_price for item in carrito_items)
    return render(request, 'Druids/carrito.html', {'carrito_items': carrito_items, 'total': total})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))  # Obtener la cantidad del formulario
    existenciaItem = CarritoItem.objects.filter(producto=producto).first() # Verificar si el producto ya está en el carrito 
    #si el producto no está en el carrito crea un nuevo item
    # si el producto ya está en el carrito aumenta la cantidad
    if existenciaItem:
        existenciaItem.cantidad += cantidad
        existenciaItem.save()
    else:
        CarritoItem.objects.create(producto=producto, cantidad=cantidad)        
    return redirect('carrito')

def disminuir_cantidad(request, carrito_item_id):
    carrito_item = get_object_or_404(CarritoItem, pk=carrito_item_id)
    if carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
    return redirect('carrito')

def aumentar_cantidad(request, carrito_item_id):

    #solo puede aumentar la cantidad si hay stock
    carrito_item = get_object_or_404(CarritoItem, pk=carrito_item_id)
    if carrito_item.cantidad < carrito_item.producto.stock:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('carrito')

def eliminar_del_carrito(request, carrito_item_id):
    carrito_item = get_object_or_404(CarritoItem, pk=carrito_item_id)
    carrito_item.delete()
    return redirect('carrito')
 
def historialCompra(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'Druids/historialCompra.html', {'pedidos': pedidos})

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

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        producto.delete()
        return redirect('inventario')
    
    context = {
        'producto': producto
    }
    return render(request, context)

def listadoProductos(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'Druids/listadoProductos.html', {'productos': productos})

def listaUsuarios(request):
    if request.method == 'POST':
        form = RegistroAdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            rol = form.cleaned_data.get('rol')
            if rol == 'Administrador':
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False

            user.save()

            print("User saved successfully")

            usuario = Usuario(
                usuario=user,
                nombre_usuario=form.cleaned_data.get('username'),
                correo=form.cleaned_data.get('email'),
                rol=rol
            )
            usuario.save()
            print("Usuario saved successfully")
            return redirect('listaUsuarios')
        else:
            print("Formulario no válido")
            print(form.errors)
    else:
        form = RegistroAdminForm()
    
    usuarios = Usuario.objects.all()
    data = {
        'usuarios': usuarios,
        'form': form
    }
    return render(request, 'Druids/listaUsuarios.html', data )

def eliminarUsuario(request,id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.usuario.delete()
    usuario.delete()
    return redirect('listaUsuarios')

def pago(request):
    carrito_items = CarritoItem.objects.all()
    total = sum(item.total_price for item in carrito_items)
    print(total)
    form = PagoForm()

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Crear el pedido
            usuario = request.user if request.user.is_authenticated else None
            pedido = Pedido(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                rut=form.cleaned_data['rut'],
                total=total,
                direccion_envio=form.cleaned_data['direccion_envio'],
                estado='Pendiente',
                usuario=usuario
            )
            pedido.save()

            # Agregar los productos al pedido
            for item in carrito_items:
                detalle_pedido = pedido.detalles.create(
                    producto=item.producto,
                    cantidad=item.cantidad,
                    precio_unitario=item.producto.precio
                )
                detalle_pedido.save()

            # Vaciar el carrito
            CarritoItem.objects.all().delete()

            return redirect('pagoexitoso')

    return render(request, 'Druids/pago.html', {'carrito_items': carrito_items, 'total': total, 'form': form})

def pagoexitoso(request):
    return render(request, 'Druids/pagoexitoso.html')

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'Druids/pedidos.html', {'pedidos': pedidos})

def detallePedido(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pedido_id = request.GET.get('id')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        detalles = DetallePedido.objects.filter(pedido=pedido)
        detalles_data = [
            {
                'producto': {
                    'nombre': detalle.producto.nombre
                },
                'cantidad': detalle.cantidad,
                'precio_unitario': detalle.precio_unitario
            } for detalle in detalles 
        ]
        data = {
            'id': pedido.id,
            'nombre': pedido.nombre,
            'apellido': pedido.apellido,
            'fecha_pedido': pedido.fecha_pedido,
            'total': pedido.total,
            'estado': pedido.estado,
            'detalles': detalles_data
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cambiar_estado_pedido(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('id')
        nuevo_estado = request.POST.get('estado')
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.estado = nuevo_estado
            pedido.save()
            return JsonResponse({'success': True})
        except Pedido.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Pedido no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def perfil(request):
    return render(request, 'Druids/perfil.html')

def producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    productos_relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)[:4]
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados
    }
    return render(request, 'Druids/producto.html',context)

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

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            usuario = Usuario(
                usuario=user,
                nombre_usuario=username,
                correo=form.cleaned_data.get('email'),
                clave=password,
                rol='Usuario'
            )
            usuario.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'Druids/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'Druids/iniciarSesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')