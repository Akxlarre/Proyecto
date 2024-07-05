$(document).ready(function() {
    console.log("Producto.js cargado");
    const decrementButton = document.querySelector('.btn-decrement');
    const incrementButton = document.querySelector('.btn-increment');
    const quantityInput = document.querySelector('#cantidad');

    if (decrementButton && incrementButton && quantityInput) {
        decrementButton.addEventListener('click', function() {
            let currentValue = parseInt(quantityInput.value);
            console.log(currentValue);
            if (currentValue > 1) {
                quantityInput.value = currentValue - 1;
            }
        });

        incrementButton.addEventListener('click', function() {
            let currentValue = parseInt(quantityInput.value);
            console.log(currentValue);
            let maxValue = parseInt(quantityInput.max);
            console.log(maxValue);
            if (currentValue < maxValue) {
                quantityInput.value = currentValue + 1;
            }
        });
    }
});