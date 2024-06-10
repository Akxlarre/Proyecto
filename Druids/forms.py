from django import forms
from .models import mensajeContacto

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

