from django import forms
from .models import Usuario, mensajeContacto , Producto
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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        return nombre
    
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not '@' in correo:
            raise forms.ValidationError('Correo inválido')
        return correo
        if not '.' in correo:
            raise forms.ValidationError('Correo inválido')
        return correo
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if len(mensaje) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres')
        return mensaje
    




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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        return precio
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        return stock
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres')
        return descripcion
    
    def clean_cuidados(self):
        cuidados = self.cleaned_data['cuidados']
        if len(cuidados) < 10:
            raise forms.ValidationError('Los cuidados deben tener al menos 10 caracteres')
        return cuidados
    


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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        return precio
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        return stock
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres')
        return descripcion
    
    def clean_cuidados(self):
        cuidados = self.cleaned_data['cuidados']
        if len(cuidados) < 10:
            raise forms.ValidationError('Los cuidados deben tener al menos 10 caracteres')
        return cuidados
    


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
    
    #sobreescribimos el método save para que guarde el email en la base de datos
    def save(self, commit=True): #commit=True significa que se guardará en la base de datos
        user_instance = super().save(commit=False)
        user_instance.email = self.cleaned_data['email']
        if commit:
            user_instance.save()
        return user_instance

class RegistroAdminForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(label='Rol', choices=[('Administrador', 'Administrador'), ('Usuario', 'Usuario')])
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rol']

    def save(self, commit=True):
        user_instance = super().save(commit=False)
        user_instance.email = self.cleaned_data['email']
        if commit:
            user_instance.save()
        return user_instance
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)



class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario','rut','correo', 'direccion' , 'foto_perfil' ]


    def save(self, commit=True):
        usuario_instance = super().save(commit=False)
        user_instance = usuario_instance.usuario
        user_instance.username = self.cleaned_data['nombre_usuario']
        user_instance.email = self.cleaned_data['correo']
        if commit:
            user_instance.save()
            usuario_instance.save()
        return usuario_instance
        


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
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 3:
            raise forms.ValidationError('El apellido debe tener al menos 3 caracteres')
        if not apellido.isalpha():
            raise forms.ValidationError('El apellido debe contener solo letras')
        return apellido
    
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if len(rut) < 8:
            raise forms.ValidationError('El RUT debe tener al menos 8 caracteres')
        if not '-' in rut:
            raise forms.ValidationError('RUT inválido')
        return rut
    
    def clean_direccion_envio(self):
        direccion_envio = self.cleaned_data['direccion_envio']
        if len(direccion_envio) < 5:
            raise forms.ValidationError('La dirección de envío debe tener al menos 5 caracteres')
        return direccion_envio
    
    def clean_nombre_titular(self):
        nombre_titular = self.cleaned_data['nombre_titular']
        if len(nombre_titular) < 3:
            raise forms.ValidationError('El nombre del titular debe tener al menos 3 caracteres')
        if not nombre_titular.isalpha():
            raise forms.ValidationError('El nombre del titular debe contener solo letras')
        return nombre_titular
    
    def clean_numero_tarjeta(self):
        numero_tarjeta = self.cleaned_data['numero_tarjeta']
        if len(numero_tarjeta) < 16:
            raise forms.ValidationError('El número de tarjeta debe tener al menos 16 caracteres')
        return numero_tarjeta
    
    def clean_fecha_expiracion(self):
        fecha_expiracion = self.cleaned_data['fecha_expiracion']
        if len(fecha_expiracion) < 5:
            raise forms.ValidationError('La fecha de expiración debe tener al menos 5 caracteres')
        if not '/' in fecha_expiracion:
            raise forms.ValidationError('Fecha de expiración inválida')
        return fecha_expiracion
    
    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        if len(cvv) < 3:
            raise forms.ValidationError('El CVV debe tener al menos 3 caracteres')
        return cvv
        if not cvv.isdigit():
            raise forms.ValidationError('El CVV debe contener solo números')
        return cvv
