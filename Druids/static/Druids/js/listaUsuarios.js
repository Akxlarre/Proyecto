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
        
        console.log("Formulario de eliminación URL:", formEliminar.attr('action'));  // debugear
    });

    // Bloquear usuario
    $('#ModalBloquear').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget);
        var usuarioId = button.data('id');
        var nombreUsuario = button.data('nombre');
        var modal = $(this);
        modal.find('.modal-body #nombreUsuarioBloquear').text(nombreUsuario);
        modal.find('#btnBloquear').click(function() {
            $.ajax({
                url: `/bloquear-usuario/${usuarioId}/`,
                type: 'GET',
                success: function(response) {
                    location.reload();
                },
                error: function(response) {
                    console.log('Error al bloquear usuario');
                }
            });
        });
    });

    // Desbloquear usuario
    $('#ModalDesbloquear').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget);
        var usuarioId = button.data('id');
        var nombreUsuario = button.data('nombre');
        var modal = $(this);
        modal.find('.modal-body #nombreUsuarioDesbloquear').text(nombreUsuario);
        modal.find('#btnDesbloquear').click(function() {
            $.ajax({
                url: `/desbloquear-usuario/${usuarioId}/`,
                type: 'GET',
                success: function(response) {
                    location.reload();
                },
                error: function(response) {
                    console.log('Error al desbloquear usuario');}
            });
        });
    });
});
