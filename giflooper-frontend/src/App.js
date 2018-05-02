import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">GifLooper</h1>
        </header>
        <div className="screenFiller">
          <p className="App-intro">
            <form>
              <label>
                searchterms:
                <input type="text" name="name" />
              </label>
              <input type="submit" value="Submit" />
            </form>
          </p>
        </div>
      </div>
    );
  }
}

export default App;
