import os
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import path, reverse
from Druids.models import CarritoItem, DetallePedido, Pedido, Producto, Usuario
from .forms import ContactoForm, EditarPerfilForm, LoginForm, PagoForm, RegistroAdminForm, RegistroProductoForm, EditarProductoForm , RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def es_superusuario(user):
    return user.is_superuser

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

    messages.success(request, 'ha sido agregado al carrito') 
    messages.success(request, print('ha sido agregado al carrito'))       
    return redirect('producto', id=producto_id)

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

def editarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    form_editar = EditarPerfilForm(instance=usuario)

    if request.method == "POST":
        form_editar = EditarPerfilForm(data=request.POST, files=request.FILES, instance=usuario)
        if form_editar.is_valid():
            form_editar.save()
            return redirect(to='listaUsuarios')

    context = {
        'formularioEditarUsuario': form_editar,
        'usuario': usuario,
    }
    return render(request, 'Druids/editarUsuario.html', context)


@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
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

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
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
    

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        # Eliminar imágenes del sistema de archivos si existen
        if producto.imagen_principal and os.path.isfile(producto.imagen_principal.path):
            os.remove(producto.imagen_principal.path)
        if producto.imagen_2 and os.path.isfile(producto.imagen_2.path):
            os.remove(producto.imagen_2.path)
        if producto.imagen_3 and os.path.isfile(producto.imagen_3.path):
            os.remove(producto.imagen_3.path)
        if producto.imagen_4 and os.path.isfile(producto.imagen_4.path):
            os.remove(producto.imagen_4.path)
        
        producto.delete()
        return redirect('inventario')
    
    context = {
        'producto': producto
    }
    return render(request, 'ruta_a_tu_template/eliminar_producto.html', context)

def listadoProductos(request, categoria):
    if categoria == 'todos':
        productos = Producto.objects.all().order_by('nombre')
    else:
        productos = Producto.objects.filter(categoria=categoria)

    return render(request, 'Druids/listadoProductos.html', {'productos': productos})

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
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

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    # Asegúrate de que 'foto_perfil' es el nombre correcto del campo en tu modelo
    foto_perfil_path = os.path.join(str(settings.MEDIA_ROOT).replace('/media/usuarios', ''), usuario.foto_perfil.name)
    
    # Remueve la foto de perfil si existe
    if os.path.isfile(foto_perfil_path):
        os.remove(foto_perfil_path)
    
    usuario.usuario.delete()
    usuario.delete()

    return redirect('listaUsuarios')

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
def bloquearUsuario(request, id):
    user = get_object_or_404(Usuario, id=id)
    print(f"Estado antes de bloquear: {user.usuario.is_active}")
    user.usuario.is_active = False
    user.usuario.save()
    print(f"Estado después de bloquear: {user.usuario.is_active}")
    return JsonResponse({'status': 'Usuario bloqueado'})

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
def desbloquearUsuario(request, id):
    user = get_object_or_404(Usuario, id=id)
    user.usuario.is_active = True
    user.usuario.save()
    return JsonResponse({'status': 'Usuario desbloqueado'})

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

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
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

@login_required
@user_passes_test(es_superusuario, login_url='/sinPermiso/')
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
    usuario = Usuario.objects.get(usuario=request.user)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario) # instance hace que el formulario se llene con los datos del usuario
        if form.is_valid():
            usuario.usuario.username = form.cleaned_data.get('nombre_usuario')
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=usuario)

    data = {
        'usuario': usuario,
        'form': form
    }
    return render(request, 'Druids/perfil.html', data)

def producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    productos_relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)[:4]
    imagenesAdicionales = [producto.imagen_2, producto.imagen_3, producto.imagen_4]
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'imagenesAdicionales': imagenesAdicionales
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
            user = authenticate(username=username, password=password) # Autenticar al usuario 
            usuario = Usuario(
                usuario=user,
                nombre_usuario=username,
                correo=form.cleaned_data.get('email'),
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
    CarritoItem.objects.all().delete()
    logout(request)
    return redirect('index')

def sinpermiso(request):
    return render(request, 'Druids/sinPermiso.html')