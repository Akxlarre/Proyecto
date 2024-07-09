const regionesYComunas = {
    "Región de Arica y Parinacota": ["Arica", "Camarones", "Putre", "General Lagos"],
    "Región de Tarapacá": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
    "Región de Antofagasta": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"],
    "Región de Atacama": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
    "Región de Coquimbo": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"],
    "Región de Valparaíso": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"],
    "Región Metropolitana": ["Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura"],
    "Región de O’Higgins": ["San Fernando","☠︎☠︎☠︎Chimbarongo☠︎☠︎☠︎","Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente"],
    "Región del Maule": ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael"],
    "Región del Ñuble": ["Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"],
    "Región del Biobío": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa"],
    "Región de La Araucanía": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol"],
    "Región de Los Ríos": ["Valdivia", "Corral", "Futrono", "La Unión", "Lago Ranco", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli"],
    "Región de Los Lagos": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Ancud", "Castro", "Chaitén", "Chonchi", "Curaco de Vélez", "Dalcahue", "Futaleufú", "Hualaihué", "Palena"],
    "Región de Aysén": ["Coyhaique", "Lago Verde", "Aysén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel"],
    "Región de Magallanes": ["Punta Arenas", "Torres del Paine", "Porvenir", "Primavera", "Timaukel", "Natales", "San Gregorio"]
};


// Función para cargar las comunas según la región seleccionada
function cargarComunas(regionSeleccionada) {
    const comunas = regionesYComunas[regionSeleccionada];
    const $selectComunas = $("#comuna");
    $selectComunas.empty(); // Limpiar opciones anteriores
    $selectComunas.append($("<option>", {
        value: "0",
        text: "Seleccione una comuna"
    }));
    $.each(comunas, function (index, comuna) {
        $selectComunas.append($("<option>", {
            value: comuna,
            text: comuna
        }));
    });
}

// Manejar el cambio en la selección de región
$("#Region").on("change", function () {
    const regionSeleccionada = $(this).val();
    cargarComunas(regionSeleccionada);
});

// Agregar la opción "Seleccione una comuna" al cargar la página
$(document).ready(function() {
    const $selectComunas = $("#comuna");
    $selectComunas.empty(); // Limpiar opciones anteriores
    $selectComunas.append($("<option>", {
        value: "0",
        text: "Seleccione una comuna"
    }));
});

// Limitar el input de fecha de expiración a números y /
$(document).ready(function() {
    $('.fecha-expiracion').on('input', function() {
        var value = $(this).val();
        // Permitir solo números y /
        value = value.replace(/[^0-9/]/g, '');
        // Limitar la longitud a 5 caracteres (MM/AA)
        if (value.length > 5) {
            value = value.substr(0, 5);
        }
        // Verificar si se ingresó '/' en el tercer dígito (mes)
        if (value.length === 3 && value[2] !== '/') {
            // Si no se ingresó '/', insertarlo automáticamente
            value = value.substr(0, 2) + '/' + value.substr(2);
        }
        $(this).val(value);
    });
});

// limitar el imput de Nombre-titular a solo letras, tildes , 1 espacio entre palabras
$(document).ready(function() {
    $('.nombre-titular').on('input', function() {
        var value = $(this).val();
        // Validar caracteres permitidos (letras, tildes y espacios)
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});

// Limitar el imput de número de tarjeta a solo números y espacios
$(document).ready(function() {
    $('.numero-tarjeta').on('input', function() {
        var value = $(this).val();
        // Permitir solo números y guiones
        value = value.replace(/[^0-9]/g, '');

        if (value.length > 16) {
            value = value.substr(0, 16);
        }

        // Eliminar guiones actuales para evitar conflictos
        value = value.replace(/-/g, '');

        // Agregar un guión después de cada grupo de cuatro dígitos
        value = value.replace(/(\d{4})/g, '$1-');

        // Eliminar un guión final si lo hay
        value = value.replace(/-$/, '');
        $(this).val(value);
    });
});

$(document).ready(function() {
    $('#zip').on('input', function() {
        var value = $(this).val();
        // Permitir solo números
        value = value.replace(/[^0-9]/g, '');
        
        if (value.length > 7) {
            value = value.substr(0, 7);
        }
        $(this).val(value);
    });
});



$(document).ready(function() {
    $('.rut').on('input', function() {
        var value = $(this).val();
        // Permitir solo números
        value = value.replace(/[^0-9kK]/g, '');
        // Formatear el rut
        value = value.replace(/(\d{1,2})(\d{3})(\d{3})([0-9kK]{1})/, '$1.$2.$3-$4');
        if (value.length > 12) {
            value = value.substr(0, 12);
        }
        $(this).val(value);
    });
});