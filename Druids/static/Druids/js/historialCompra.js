$(document).ready(function() {
    $('.ver-detalles').on('click', function() {
        var pedidoId = $(this).data('pedido-id');
        console.log('Pedido ID: ' + pedidoId);
        $.ajax({
            url: detallePedidoUrl,
            method: 'GET',
            data: { id: pedidoId },
            success: function(data) {
                // Asignar los datos al modal
                $('#modalVerPedido' + pedidoId + ' #pedido-id').text(data.id);
                var detallesHtml = '';
                data.detalles.forEach(function(detalle) {
                    subtotal = detalle.producto.precio * detalle.cantidad;
                    detallesHtml += '<li>' + detalle.producto.nombre + ' x' + detalle.cantidad +' </li>';
                });
                console.log(detallesHtml);
                $('#modalVerPedido' + pedidoId + ' #listaProductos').html(detallesHtml);
            }
        });
    });
});