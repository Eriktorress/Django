$("#formLogin").validate({
    rules:{
      username: "required",
      password: "required"
    },
    messages: {
      username: "Favor ingresar el nombre de usuario",
      password: "Favor ingresar la contraseña"
    }
  });

$("#formRegistro").validate({
  rules:{
    username: {
      required: true,
      minlength: 5,
      maxlength: 10
    },
    email: {
      required: true,
      email: true
    },
    password1: {
      required: true,
      minlength: 10
    },
    password2:  {
      required: true,
      minlength: 10,
      equalTo: "#password1"
    },
  },
  messages: {
    username: {
      minlength: "Ingrese un Minimo de 5 caracteres",
      maxlength: "Debe contener maximo 10 caracteres"
    },
  }
});