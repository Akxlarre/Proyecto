// Esperamos 1 segundo antes de mostrar el título
setTimeout(function() {
    var tituloItem = document.getElementById('tituloItem');
    tituloItem.classList.add('visible');
}, 500);

// Esperamos 3 segundos antes de mostrar el texto, para que aparezca después del título
setTimeout(function() {
    var textoItem = document.getElementById('textoItem');
    textoItem.classList.add('visible');
}, 2000); 

setTimeout(function() {
    var imagenItem = document.getElementById('imagen-item-1');
    imagenItem.classList.add('visible');
}, 2100);

