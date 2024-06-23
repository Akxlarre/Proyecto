$(document).ready(function(){
    var modalEliminar = $('#ModalEliminar');

    modalEliminar.on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var usuarioid = button.data('id');
        var usuarioname = button.data('nombre');
        
        var modalBody = modalEliminar.find('.modal-body #nombreUsuario');
        var formEliminar = modalEliminar.find('#formEliminar');
        
        modalBody.text(usuarioname);
        formEliminar.attr('action', `/eliminar_usuario/${usuarioid}/`);
        
        console.log("Formulario de eliminación URL:", formEliminar.attr('action'));  // Debugging line
    });
});