import { Component } from 'react';
import './App.css';

class StringGen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      genButton: 'Generate',
      genStatus: 'Ready...',
      downloadURL: 'http://localhost:5000/download',
      report: {
        alphabetical: 0,
        real_number: 0,
        integer: 0,
        alphanumeric: 0
      },
      showLink: false
    }
    this.generateString = this.generateString.bind(this)
    this.getReport = this.getReport.bind(this)
  }

  generateString() {
    let self = this;
    let genButton = 'Loading...'
    let genStatus = 'Loading...'
    self.setState({genButton, genStatus})
    fetch('http://localhost:5000/generate')
    .then(res => res.json())
    .then(json => {
      genStatus = json.status
      let showLink = true
      genButton = 'Generate'
    	self.setState({genStatus, genButton, showLink});
    });
  }

  getReport() {
    let self = this;
    fetch('http://localhost:5000/report')
    .then(res => res.json())
    .then(json => {
      let report = json.data;
    	self.setState({report});
    });
  }

  render() {
    return (
      <div>
        <div>
          <button disabled={this.state.genButton === 'Loading...'} onClick={this.generateString}>{this.state.genButton}</button>
        </div>
        <p>
          <span>{this.state.genStatus}</span>
        </p>
        { this.state.showLink ? 
        <p>
          <a className="App-link" href={this.state.downloadURL}>{this.state.downloadURL}</a>
        </p> 
        : null }
        <div>
          <button onClick={this.getReport}>Report</button>
        </div>
        <p>Alphabetical: {this.state.report.alphabetical}</p>
        <p>Real Number: {this.state.report.real_number}</p>
        <p>Integer: {this.state.report.integer}</p>
        <p>Alphanumeric: {this.state.report.alphanumeric}</p>
      </div>
    );
  }
}

export default StringGen;