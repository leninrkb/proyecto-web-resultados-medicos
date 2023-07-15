export function calcularEdad(fechaNacimiento) {
    const fechaActual = new Date();
    const fechaNac = new Date(fechaNacimiento);
    
    let edad = fechaActual.getFullYear() - fechaNac.getFullYear();
    
    const mesActual = fechaActual.getMonth();
    const diaActual = fechaActual.getDate();
    const mesNac = fechaNac.getMonth();
    const diaNac = fechaNac.getDate();
    
    if (mesActual < mesNac || (mesActual === mesNac && diaActual < diaNac)) {
      edad--;
    }
    
    return edad;
  }