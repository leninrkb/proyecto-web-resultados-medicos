import CryptoJS from 'crypto-js';


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


export function encodeBase64(datos) {
  var datos = CryptoJS.enc.Utf8.parse(datos.toString());
  return CryptoJS.enc.Base64.stringify(datos);

}

export function decodeBase64(datos) {
  var datos = CryptoJS.enc.Base64.parse(datos);
  return CryptoJS.enc.Utf8.stringify(datos);
}


export function cifrar(datos, llave) {
  let cifrado  = CryptoJS.AES.encrypt(datos, llave).toString();
  cifrado = encodeBase64(cifrado);
  return cifrado;
}

export function descifrar(cifrado, llave) {
  cifrado = decodeBase64(cifrado);
  let descifrado = CryptoJS.AES.decrypt(cifrado, llave).toString(CryptoJS.enc.Utf8);
  return descifrado;
}