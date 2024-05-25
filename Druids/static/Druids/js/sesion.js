$(document).ready(function() {
    // Verificar si el botón estaba oculto en la página anterior
    var sesion = localStorage.getItem('sesion');
    if (sesion === 'true') {
        $('#boton-inicio-sesion').hide();
        $('#boton-perfil').show();
        $('#mySidenav').show();
    }
    if (sesion === 'false') {
        $('#boton-inicio-sesion').show();
        $('#boton-perfil').hide();
        $('#mySidenav').hide();
    }

    $('#formulario-inicio-sesion').submit(function(event) {
        localStorage.setItem('sesion', 'true');
    });

    $('#cerrar-sesion').click(function() {
        $('#boton-inicio-sesion').show();
        $('#boton-perfil').hide();
        $('#mySidenav').hide();
        localStorage.setItem('sesion', 'false');
    });
});