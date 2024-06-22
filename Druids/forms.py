from django import forms
from .models import mensajeContacto , Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactoForm(forms.ModelForm):
    class Meta:
        model = mensajeContacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'nombre-contacto', 
                'placeholder': 'Ingresa tu nombre'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control', 
                'id': 'email-contacto', 
                'placeholder': 'Ingresa tu correo'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'mensaje-contacto', 
                'rows': 3,
                'placeholder': 'Escribe tu mensaje'
            }),
        }

class RegistroProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'stock', 'descripcion', 'cuidados', 'imagen_principal', 'imagen_2', 'imagen_3', 'imagen_4']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'nombre-producto', 
                'placeholder': 'Nombre del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'precio-producto', 
                'placeholder': 'Precio del producto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control', 
                'id': 'categoria-producto'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'stock-producto', 
                'placeholder': 'Stock del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'descripcion-producto', 
                'rows': 3,
                'placeholder': 'Descripción del producto'
            }),
            'cuidados': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'cuidados-producto', 
                'rows': 3,
                'placeholder': 'Cuidados del producto'
            }),
            'imagen_principal': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-principal-producto'
            }),
            'imagen_2': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-2-producto'
            }),
            'imagen_3': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-3-producto'
            }),
            'imagen_4': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-4-producto'
            }),
        }

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'stock', 'descripcion', 'cuidados', 'imagen_principal', 'imagen_2', 'imagen_3', 'imagen_4']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'nombre-producto', 
                'placeholder': 'Nombre del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'precio-producto', 
                'placeholder': 'Precio del producto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control', 
                'id': 'categoria-producto'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'stock-producto', 
                'placeholder': 'Stock del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'descripcion-producto', 
                'rows': 3,
                'placeholder': 'Descripción del producto'
            }),
            'cuidados': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'cuidados-producto', 
                'rows': 3,
                'placeholder': 'Cuidados del producto'
            }),
            'imagen_principal': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-principal-producto'
            }),
            'imagen_2': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-2-producto'
            }),
            'imagen_3': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-3-producto'
            }),
            'imagen_4': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imagen-4-producto'
            }),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class PagoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')
    rut = forms.CharField(label='RUT', max_length=10)
    direccion_envio = forms.CharField(label='Dirección de Envío', max_length=255)
    metodo_pago = forms.ChoiceField(label='Método de Pago', choices=[('credito', 'Tarjeta de Crédito'), ('debito', 'Tarjeta de Débito')])
    nombre_titular = forms.CharField(label='Nombre del Titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de Tarjeta', max_length=16)
    fecha_expiracion = forms.CharField(label='Vencimiento', max_length=5)
    cvv = forms.CharField(label='CVV', max_length=3)
    