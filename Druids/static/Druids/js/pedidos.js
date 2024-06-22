$(document).ready(function() {
    $('.ver-detalles').on('click', function() {
        var pedidoId = $(this).data('pedido-id');
        $.ajax({
            url: detallePedidoUrl,
            method: 'GET',
            data: { id: pedidoId },
            success: function(data) {
                // Asignar los datos al modal
                $('#modalVerPedido' + pedidoId + ' #pedido-id').text(data.id);
                $('#modalVerPedido' + pedidoId + ' #pedido-cliente').text(data.nombre + ' ' + data.apellido);
                $('#modalVerPedido' + pedidoId + ' #pedido-fecha').text(data.fecha_pedido);
                $('#modalVerPedido' + pedidoId + ' #pedido-total').text(data.total);
                $('#modalVerPedido' + pedidoId + ' #pedido-estado').text(data.estado);

                var detallesHtml = '';
                data.detalles.forEach(function(detalle) {
                    subtotal = detalle.precio_unitario * detalle.cantidad;
                    detallesHtml += '<tr>' +
                                    '<td>' + detalle.producto.nombre + '</td>' +
                                    '<td>' + detalle.cantidad + '</td>' +
                                    '<td>$' + detalle.precio_unitario + '</td>' +
                                    '<td>$' + subtotal + '</td>' +
                                    '</tr>';
                });
                $('#modalVerPedido' + pedidoId + ' #pedido-detalles').html(detallesHtml);

                $('#modalVerPedido' + pedidoId).modal('show');
            }
        });
    });
        // Manejar cambio de estado del pedido
    $('.cambiar-estado').on('click', function() {
        var pedidoId = $(this).data('pedido-id');
        var nuevoEstado = $(this).data('estado');
        $.ajax({
            url: cambiarEstadoPedidoUrl,
            method: 'POST',
            data: {
                id: pedidoId,
                estado: nuevoEstado,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.success) {
                    location.reload(); // Recargar la página para reflejar los cambios
                } else {
                    alert('Error: ' + response.error);
                }
            }
        });
    });
});
