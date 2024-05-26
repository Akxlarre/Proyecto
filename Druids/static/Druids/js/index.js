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

setTimeout(function() {
    var sabermas = document.getElementById('boton-saber-mas');
    sabermas.classList.add('visible');
}, 2500)

setTimeout(function() {
    var textoSaberMas = document.getElementById('texto-saber-mas');
    textoSaberMas.classList.add('visible');
}, 2500);