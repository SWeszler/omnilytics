import logo from './logo.svg';
import './App.css';
import StringGen from './StringGen'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          Generate Strings
        </h1>
      </header>
      <StringGen></StringGen>
    </div>
  );
}

export default App;
