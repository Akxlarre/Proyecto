from .models import CarritoItem

def carrito_items_contador(request):
    if request.user.is_authenticated:
        contador = CarritoItem.objects.filter(usuario=request.user).count()
    else:
        contador = CarritoItem.objects.count()
    return {'carrito_items_contador': contador}