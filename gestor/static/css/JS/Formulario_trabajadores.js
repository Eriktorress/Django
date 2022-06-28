
$.validator.addMethod ("terminarPor",function(value,element,parametro) {

  if(value.endsWith(parametro)){
    return true;
  }
  return false;
},"Debe terminar por {0}")


$("#formTrabajador").validate({
      rules:{
        nombre: {
          required: true,
          minlength: 5,
          maxlength: 15
        },

        apellido: {
          required: true,
          minlength: 5,
          maxlength: 15
        },

        rut:{
          required:true,
          minlength: 11,
          maxlength: 12
        },

        email:{
        required: true,
        email: true,
        terminarPor:"duocuc.cl"
        }
      },
      messages: {
        nombre: {
          required: " *Campo obligatorio" ,
          minlength: "Ingrese un Minimo de 5 caracteres",
          maxlength: "Debe contener maximo 15 caracteres"
        },
        apellido: {
          required: " *Campo obligatorio",
          minlength: "Ingrese un Minimo de 5 caracteres",
          maxlength: "Debe contener maximo 15 caracteres"
        },
        rut: {
          required: " *Campo obligatorio"
        },
        email: {
          required: " *Campo obligatorio",
          email: "ingresar un formato valido"
        },
      }
});