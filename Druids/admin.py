from django.contrib import admin
from .models import Usuario, Producto, Pedido, DetallePedido

class adminUsuario(admin.ModelAdmin):
    list_display = ['nombre_usuario', 'rut', 'correo', 'rol']
    search_fields = ['nombre_usuario', 'rut', 'correo']
    list_filter = ['rol']

class adminProducto(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'stock']
    search_fields = ['nombre', 'precio', 'categoria']
    list_filter = ['categoria']

class adminPedido(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'rut', 'fecha_pedido', 'total', 'estado']
    search_fields = ['nombre', 'apellido', 'email', 'rut', 'fecha_pedido', 'total']
    list_filter = ['estado']

class adminDetallePedido(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio_unitario']
    search_fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']



admin.site.register(Usuario, adminUsuario)
admin.site.register(Producto, adminProducto)
admin.site.register(Pedido, adminPedido)
admin.site.register(DetallePedido, adminDetallePedido)
