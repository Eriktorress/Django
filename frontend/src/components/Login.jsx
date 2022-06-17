import React from "react"

export const Login = () => {
    return (
      
        <div className="container" style={{background:"lightgray", marginTop:20, padding:20}}>
        
            <form id="form_login">
                <div>
                    <h1 style={{color:"blue", textalign:"center"}}>LOGIN</h1>
                    <label htmlFor="txtusu"><strong>Username</strong></label>
                    <input type="text" id="txtusu" style={{textAlign:"center"}} className="form-control"  required/>
                </div>
                <div>
                    <label htmlFor="txtpas"><strong>Password</strong></label>
                    <input type="password" id="txtpas" style={{textAlign:"center"}} className="form-control"  required/>
                </div><br/>
                <input type="submit"  className="btn btn-primary" value="Login"/>
            </form>

        </div>
        
    )
}
