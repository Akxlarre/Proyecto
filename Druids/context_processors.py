from .models import CarritoItem

def carrito_items_contador(request):
    contador = CarritoItem.objects.count()
    return {'carrito_items_contador': contador}