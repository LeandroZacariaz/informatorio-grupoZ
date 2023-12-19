function guardarPosicionDesplazamiento() {
    localStorage.setItem('scrollPosition', window.scrollY);
}

// Obtener la posición de desplazamiento almacenada en el almacenamiento local
var scrollPosition = localStorage.getItem('scrollPosition');

// Restaurar la posición de desplazamiento si está disponible
if (scrollPosition !== null) {
    window.scrollTo(0, scrollPosition);
}

function mostrarCat(){
    document.getElementById('cat-ocultas').style.display='block';
    document.getElementById('alf-ocultas').style.display='none';
    document.getElementById('fechas-ocultas').style.display='none';
}
function ocultarCat(){
    document.getElementById('cat-ocultas').style.display='none';
}
function mostrarAlf(){
    document.getElementById('alf-ocultas').style.display='block';
    document.getElementById('cat-ocultas').style.display='none';
    document.getElementById('fechas-ocultas').style.display='none';
}
function ocultarAlf(){
    document.getElementById('alf-ocultas').style.display='none';
}
function mostrarFec(){
    document.getElementById('fechas-ocultas').style.display='block';
    document.getElementById('cat-ocultas').style.display='none';
    document.getElementById('alf-ocultas').style.display='none';
}
function ocultarFec(){
    document.getElementById('fechas-ocultas').style.display='none';
}

let antiguo=0;
function mostrarEdit(idcom){
    
    if ((idcom!=antiguo)&&(antiguo!=0)){
        
        document.getElementById(antiguo).style.display='none';
    }
    
    document.getElementById(idcom).style.display='block';
    
    antiguo=idcom;
    
}



