$(document).ready(function() {
    // Sidebar
    // al hacer hover en el sidebar la imagen desaparece
    $('#text-inventario').hide();
    $('#inventario').hover(function() {
        $('#img-inventario').hide();
        $('#text-inventario').show();
    },
    function() {
        $('#img-inventario').show();
        $('#text-inventario').hide();
    });

    $('#text-pedidos').hide();
    $('#pedidos').hover(function() {
        $('#img-pedidos').hide();
        $('#text-pedidos').show();
    },
    function() {
        $('#img-pedidos').show();
        $('#text-pedidos').hide();
    });

    $('#text-usuarios').hide();
    $('#usuarios').hover(function() {
        $('#img-usuarios').hide();
        $('#text-usuarios').show();
    },
    function() {
        $('#img-usuarios').show();
        $('#text-usuarios').hide();
    });
});
