import React from 'react'
import '../Css/inicio_sesion.css';
import { Link } from "react-router-dom";

export const Login = () => {
    return (
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
                            <input type="text" placeholder="Correo Electronico" />
                            <input type="password" placeholder="Contraseña" />
                            <button type="button" class="btn btn-primary width-100"> Entrar </button>
                            <nav>
                                <Link to="/Dashboard.jsx"><button type="button" class="btn btn-primary width-100"> Entrar </button></Link>
                            </nav>
                        </form>
                         {/* Registrar  */}
                        <form action="" class="formulario__register">
                            <h2>Regístrarse</h2>
                            <input type="username" placeholder="Nombre completo" />
                            <input type="email" placeholder="Correo Electronico" />
                            <input type="password1" placeholder="Usuario" />
                            <input type="password2" placeholder="Contraseña" />
                            <button>Regístrarse</button>
                        </form>
                    </div>
                </div>

            </div>

        </div>
    )
}
