from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


Categorias = [
    ('Arboles', 'Arboles'),
    ('Arbustos', 'Arbustos'),
    ('Cactus', 'Cactus'),
    ('Flores', 'Flores'),
    ('Implementos', 'Implementos'),
    ('Cuidados', 'Cuidados'),
    ('Enredaderas', 'Enredaderas'),   
]

class Usuario(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50, unique=True, verbose_name="Nombre de usuario")
    rut = models.CharField(max_length=10, unique=True, verbose_name="RUT", blank=True, null=True)
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    foto_perfil = models.ImageField(upload_to='usuarios/', blank=True, null=True, verbose_name="Foto de perfil")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    rol = models.CharField(max_length=20, choices=[('Administrador', 'Administrador'), ('Usuario', 'Usuario')], verbose_name="Rol")

    def __str__(self):
        return f"{self.nombre_usuario} - {self.correo}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    precio = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    categoria = models.CharField(max_length=50, choices=Categorias, verbose_name="Categoría")
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name="Stock")
    descripcion = models.TextField(verbose_name="Descripción del producto")
    cuidados = models.TextField(verbose_name="Descripción de cuidados",blank=True, null=True)
    imagen_principal = models.ImageField(upload_to='productos/', verbose_name="Imagen Principal")
    imagen_2 = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del producto 2")
    imagen_3 = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del producto 3")
    imagen_4 = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del producto 4")

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del cliente")
    email = models.EmailField(verbose_name="Correo Electrónico")
    rut = models.CharField(max_length=10, verbose_name="RUT")
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del pedido")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    direccion_envio = models.CharField(max_length=255, verbose_name="Dirección de envío")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')], verbose_name="Estado")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)
    

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.nombre_usuario} - {self.total}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
    
class mensajeContacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    mensaje = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
    
class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.cantidad} of {self.producto.nombre}'

    @property
    def total_price(self):
        return self.cantidad * self.producto.precio