from django.urls import path, include

from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('carrito/', carrito, name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('disminuir_cantidad/<int:carrito_item_id>/', disminuir_cantidad, name='disminuir_cantidad'),
    path('aumentar_cantidad/<int:carrito_item_id>/', aumentar_cantidad, name='aumentar_cantidad'),
    path('eliminar_del_carrito/<int:carrito_item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('historialCompra/', historialCompra, name='historialCompra'),
    path('inventario/', inventario, name='inventario'),
    path('listadoProductos/<str:categoria>/', listadoProductos, name='listadoProductos'),
    path('listaUsuarios/', listaUsuarios, name='listaUsuarios'),
    path('eliminar_usuario/<int:id>/', eliminarUsuario, name='eliminar_usuario'),
    path('pago/', pago, name='pago'),
    path('pagoexitoso/', pagoexitoso, name='pagoexitoso'),
    path('pedidos/', pedidos, name='pedidos'),
    path('detallePedido/', detallePedido, name='detallePedido'),
    path('cambiarEstadoPedido/', cambiar_estado_pedido, name='cambiarEstadoPedido'),
    path('perfil/', perfil, name='perfil'),
    path('producto/<int:id>/', producto, name='producto'),
    path('sobreNosotros/', sobreNosotros, name='sobreNosotros'),
    path('contacto/', Contacto, name='contacto'),
    path('editarProducto/<int:id>/', editarProducto, name='editarProducto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('iniciarSesion/', iniciar_sesion, name='iniciarSesion'),
    path('cerrarSesion/', cerrar_sesion, name='cerrarSesion'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)