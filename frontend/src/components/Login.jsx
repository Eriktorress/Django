import React, { useState } from 'react'
import '../Css/inicio_sesion.css';
import { Link } from "react-router-dom";
import { Dashboard } from './Dashboard';



export const Login = () => {

    const [miLogin, setMiLogin] = useState("false");
    const [usu, setUsu] = useState("");
    const [pas, setPas] = useState("");


    function iniciarSesion(e) {
        e.preventDefault();
        var txtusu = document.getElementById("txtusu").value;
        var txtpas = document.getElementById("txtpas").value;
        if (txtusu.minlength > 5|| txtpas.minlength > 5) { //conntrola contraseña y usuario
            alert("Complete Los Datos Faltantes!!");
        }else{
            if(usu === "admin" && pas==="123"){
              setMiLogin("true");
              document.getElementById("contenedor__todo")
              window.location.href ="/Dashboard";
            }else{
              setMiLogin("false");
              alert("Error De Usuario y/o Contraseña!!");
              document.getElementById("txtusu").value = "";
              document.getElementById("txtpas").value = "";
              document.getElementById("txtusu").focus();
              
            }
          }
        }

return (

    <main>
        <div>
            <div className="contenedor__todo">

                <div class="contenedor__todo">
                    <div class="caja__trasera">
                        <div class="caja__trasera-login">
                            <h2 >¿Ya tienes cuenta?</h2>
                            <p> Inicia sesión para entrar en la página </p>
                            <button id="btn__iniciar-sesion">Iniciar Sesión</button>
                        </div>
                        <div class="caja__trasera-register">
                            <h3>¿Aún no tienes una cuenta?</h3>
                            <p>Regístrate para que puedas iniciar sesión</p>
                            <button id="btn__registrarse">Regístrarse</button>
                        </div>
                    </div>
                    {/* Formulario de Login y registro */}
                    <div class="contenedor__login-register">
                        {/* Login  */}
                        <form action="" class="formulario__login">
                            <h2>Iniciar Sesión</h2>
                            <input type="text" placeholder="Correo Electronico" htmlFor="txtusu" id="txtusu" onChange={(e) => setUsu(e.target.value)} />
                            <input type="password" placeholder="Contraseña" htmlFor="txtpas" id="txtpas" onChange={(e) => setPas(e.target.value)} />
                            <input type="button"  className="btn btn-primary" value="Login" onClick={ iniciarSesion }/>
                            
                            <button type="button" onClick={iniciarSesion} class="btn btn-primary width-100"> Entrar </button>
                     
                        </form>
                        {/* Registrar  */}
                        <form action="" class="formulario__register">
                            <h2>Regístrarse</h2>
                            <input type="username" placeholder="Nombre completo" required />
                            <input type="email" placeholder="Correo Electronico" required />
                            <input type="password1" placeholder="Usuario" required />
                            <input type="password2" placeholder="Contraseña" required />
                            <button>Regístrarse</button>
                        </form>

                        { miLogin === "true" && <Dashboard usu={usu}/> }
                    </div>
                </div>

            </div>

        </div>


    </main>


)
}
