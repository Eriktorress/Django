
//import logo from './logo.svg';
import './App.css';

import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Login } from './components/Login'

function App() {
  return (
    <div className="App">
      
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Login/>}/>
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;