import logo from './logo.svg';
import './App.css';
import { Routes, Route, Link } from "react-router-dom";
import { Login } from './components/Login';
import { Dashboard } from './components/Dashboard';


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="Login" element={<Login />} />
        <Route path="Dasboard" element={<Dashboard />} />
      </Routes>
    </div>
  );
}
// App.js
function Home() {
  return (
    <>
      <main>
        <h2>Welcome to the homepage!</h2>
        <p>You can do this, I believe in you.</p>
      </main>
      <nav>
        <Link to="/Login">Login</Link>
      </nav>
    </>
  );
}

function about() {
  return (
    <>
      <main>
        <h2>Who are we?</h2>
        <p>
          That feels like an existential question, don't you
          think?
        </p>
      </main>
      <nav>
        <Link to="/Dashboard">Home</Link>
      </nav>
    </>
  );
}


export default App;
