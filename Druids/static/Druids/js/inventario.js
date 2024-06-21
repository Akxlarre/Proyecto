$(document).ready(function(){
    var modalEliminarProducto = $('#modalEliminarProducto');

    modalEliminarProducto.on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var productId = button.data('id');
        var productName = button.data('nombre');
        
        var modalBody = modalEliminarProducto.find('.modal-body #productoNombre');
        var formEliminar = modalEliminarProducto.find('#formEliminar');
        
        modalBody.text(productName);
        formEliminar.attr('action', `/eliminar_producto/${productId}/`);
        
        console.log("Formulario de eliminación URL:", formEliminar.attr('action'));  // Debugging line
    });
});