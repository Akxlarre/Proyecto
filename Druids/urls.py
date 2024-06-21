from django.urls import path, include

from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('carrito/', carrito, name='carrito'),
    path('historialCompra/', historialCompra, name='historialCompra'),
    path('inventario/', inventario, name='inventario'),
    path('listadoProductos/', listadoProductos, name='listadoProductos'),
    path('listaUsuarios/', listaUsuarios, name='listaUsuarios'),
    path('pago/', pago, name='pago'),
    path('pagoexitoso/', pagoexitoso, name='pagoexitoso'),
    path('pedidos/', pedidos, name='pedidos'),
    path('perfil/', perfil, name='perfil'),
    path('producto/', producto, name='producto'),
    path('sobreNosotros/', sobreNosotros, name='sobreNosotros'),
    path('contacto/', Contacto, name='contacto'),
    path('editarProducto/<int:id>/', editarProducto, name='editarProducto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)