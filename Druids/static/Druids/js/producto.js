$(document).ready(function() {
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            // Selecciona todas las alertas que deben desvanecerse
            var alerts = document.querySelectorAll('.alert.auto-dismiss');
            alerts.forEach(function(alert) {
                // Usa el método bootstrap de jQuery para cerrar la alerta
                $(alert).alert('close');
            });
        }, 2000);
    });
});