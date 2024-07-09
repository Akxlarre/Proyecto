import re #importe la librería de expresiones regulares para validar los campos de los formularios
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
        if len(nombre) > 50:
            raise forms.ValidationError('El nombre no puede exceder los 50 caracteres')
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            raise forms.ValidationError('El nombre debe contener solo letras y espacios')
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            raise forms.ValidationError('Correo inválido')
        return correo

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if len(mensaje) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres')
        if len(mensaje) > 500:
            raise forms.ValidationError('El mensaje no puede exceder los 500 caracteres')
        return mensaje
    




class RegistroProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'descripcion', 'cuidados']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'cuidados': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        if len(nombre) > 100:
            raise forms.ValidationError('El nombre no puede exceder los 100 caracteres')
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            raise forms.ValidationError('El nombre debe contener solo letras y espacios')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        if precio > 10000:
            raise forms.ValidationError('El precio no puede exceder los $10,000')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        if stock > 10000:
            raise forms.ValidationError('El stock no puede exceder las 10,000 unidades')
        return stock

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres')
        if len(descripcion) > 1000:
            raise forms.ValidationError('La descripción no puede exceder los 1000 caracteres')
        return descripcion

    def clean_cuidados(self):
        cuidados = self.cleaned_data['cuidados']

        if cuidados is not None:
            if len(cuidados) < 10:
                raise forms.ValidationError('Los cuidados deben tener al menos 10 caracteres')
            if len(cuidados) > 1000:
                raise forms.ValidationError('Los cuidados no pueden exceder los 1000 caracteres')
            return cuidados
        else:
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
        if len(nombre) > 100:
            raise forms.ValidationError('El nombre no puede exceder los 100 caracteres')
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            raise forms.ValidationError('El nombre debe contener solo letras y espacios')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        if precio > 10000:
            raise forms.ValidationError('El precio no puede exceder los $10,000')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        if stock > 10000:
            raise forms.ValidationError('El stock no puede exceder las 10,000 unidades')
        return stock

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres')
        if len(descripcion) > 1000:
            raise forms.ValidationError('La descripción no puede exceder los 1000 caracteres')
        return descripcion

    def clean_cuidados(self):
        cuidados = self.cleaned_data['cuidados']
        if cuidados is not None:
            if len(cuidados) < 10:
                raise forms.ValidationError('Los cuidados deben tener al menos 10 caracteres')
            if len(cuidados) > 1000:
                raise forms.ValidationError('Los cuidados no pueden exceder los 1000 caracteres')
            return cuidados
        else:
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
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        if len(username) > 30:
            raise forms.ValidationError('El nombre de usuario no puede exceder los 30 caracteres')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('El nombre de usuario contiene caracteres no permitidos')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError('Correo inválido')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        if len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un número')
        if not re.search(r'[\W_]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un símbolo')
        return password2

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
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        if len(username) > 30:
            raise forms.ValidationError('El nombre de usuario no puede exceder los 30 caracteres')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('El nombre de usuario contiene caracteres no permitidos')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError('Correo inválido')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        if len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un número')
        if not re.search(r'[\W_]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un símbolo')
        return password2
    

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
    
    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data['nombre_usuario']
        if len(nombre_usuario) < 3:
            raise forms.ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        if len(nombre_usuario) > 30:
            raise forms.ValidationError('El nombre de usuario no puede exceder los 30 caracteres')
        if not re.match(r'^[\w.@+-]+$', nombre_usuario):
            raise forms.ValidationError('El nombre de usuario contiene caracteres no permitidos')
        return nombre_usuario

    def clean_rut(self):
        rut = self.cleaned_data['rut']

        if rut is not None:
            if not re.match(r'^\d{1,8}-[kK\d]$', rut):
                raise forms.ValidationError('Formato de RUT inválido')
            return rut
        else:
            return rut

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            raise forms.ValidationError('Correo inválido')
        return correo

    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']

        if direccion is not None:
            if len(direccion) < 5:
                raise forms.ValidationError('La dirección debe tener al menos 5 caracteres')
            if len(direccion) > 255:
                raise forms.ValidationError('La dirección no puede exceder los 255 caracteres')
            return direccion
        else:
            return direccion

    def clean_foto_perfil(self):
        foto_perfil = self.cleaned_data['foto_perfil']

        if foto_perfil is not None:
            if foto_perfil.size > 5 * 1024 * 1024:
                raise forms.ValidationError('El tamaño de la foto no puede exceder los 5MB')
            if not foto_perfil.name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG', '.JPEG', '.PNG', '.GIF')):
                raise forms.ValidationError('El archivo debe ser una imagen en formato JPG, JPEG, PNG o GIF')
            return foto_perfil
        else:
            return foto_perfil
        


class PagoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')
    rut = forms.CharField(label='RUT', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control rut', 'placeholder': '12345678-9'}))
    direccion_envio = forms.CharField(label='Dirección de Envío', max_length=255)
    metodo_pago = forms.ChoiceField(label='Método de Pago', choices=[('credito', 'Tarjeta de Crédito'), ('debito', 'Tarjeta de Débito')])
    nombre_titular = forms.CharField(label='Nombre del Titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de Tarjeta', max_length=19, widget=forms.TextInput(attrs={'class': 'form-control numero-tarjeta', 'placeholder': 'XXXX-XXXX-XXXX-XXXX'}))
    fecha_expiracion = forms.CharField(label='Vencimiento', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control fecha-expiracion', 'placeholder': 'MM/YY'})) 
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
        
        # Limpiar el RUT eliminando puntos y espacios
        rut = rut.replace('.', '').replace(' ', '')
        
        # Verificar longitud mínima
        if len(rut) < 8:
            raise forms.ValidationError('El RUT debe tener al menos 8 caracteres')
        
        # Verificar formato correcto (número y guión)
        if '-' not in rut or rut.count('-') > 1:
            raise forms.ValidationError('RUT inválido')
        
        # Separar número y dígito verificador
        rut_number, verificador = rut.split('-')
        
        # Verificar que el número sea numérico y el verificador sea un dígito o 'k' (para RUTs válidos)
        if not (rut_number.isdigit() and (verificador.isdigit() or verificador.lower() == 'k')):
            raise forms.ValidationError('RUT inválido')
        
        # Convertir el dígito verificador calculado a string
        suma = 0
        factor = 2
        rut_number = int(rut_number)
        
        # Algoritmo para calcular el dígito verificador
        while rut_number > 0:
            suma += (rut_number % 10) * factor
            rut_number //= 10
            factor = factor % 7 + 1
        
        resto = suma % 11
        dv_calculado = 11 - resto if resto != 1 else 0
        
        # Manejar el caso especial de 'k' en mayúscula
        if dv_calculado == 10:
            dv_calculado = 'k'
        
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
        numero_tarjeta = numero_tarjeta.replace('-', '')
        def luhn_algorithm(n):
            r = [int(ch) for ch in str(n)][::-1]
            return sum(r[0::2] + [sum(divmod(d*2, 10)) for d in r[1::2]]) % 10 == 0
        if len(numero_tarjeta) < 16:
            raise forms.ValidationError('El número de tarjeta debe tener al menos 16 caracteres')
        if not numero_tarjeta.isdigit():
            raise forms.ValidationError('El número de tarjeta debe contener solo números')
        else:
            if not luhn_algorithm(numero_tarjeta):
                raise forms.ValidationError('Número de tarjeta inválido')
        return numero_tarjeta
    
    def clean_fecha_expiracion(self):
        fecha_expiracion = self.cleaned_data['fecha_expiracion']
        if not fecha_expiracion:
            raise forms.ValidationError('La fecha de expiración es requerida.')

        # Verifica si la fecha de expiración está en el formato esperado 'MM/YY'
        if '/' not in fecha_expiracion:
            raise forms.ValidationError('El formato de la fecha de expiración debe ser MM/YY.')

        try:
            month, year = fecha_expiracion.split('/')
        except ValueError:
            raise forms.ValidationError('Formato de fecha de expiración inválido.')
        if not (1 <= int(month) <= 12):
            raise forms.ValidationError('Mes inválido')
        if int(year) < 23:  # Asume que no se aceptan tarjetas expiradas antes de 2023
            raise forms.ValidationError('Año inválido')
        return fecha_expiracion
    
    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        if len(cvv) < 3:
            raise forms.ValidationError('El CVV debe tener al menos 3 caracteres')
        return cvv
        if not cvv.isdigit():
            raise forms.ValidationError('El CVV debe contener solo números')
        return cvv
