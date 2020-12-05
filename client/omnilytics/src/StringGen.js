import { Component } from 'react';
import './App.css';

const API_URL = 'http://localhost:5000/'

class StringGen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      genStatus: 'Ready...',
      downloadURL: API_URL + 'download/',
      report: {
        alphabetical: 0,
        real_number: 0,
        integer: 0,
        alphanumeric: 0
      },
      showLink: false,
      showReport: false
    }
    this.generateString = this.generateString.bind(this)
    this.getReport = this.getReport.bind(this)
  }

  generateString() {
    let self = this;
    let genStatus = 'Loading...'
    let showLink = false
    let showReport = false
    let timeStamp = Date.now()
    self.setState({genStatus, showLink, showReport, timeStamp})
    fetch(API_URL + 'generate/' + timeStamp)
    .then(res => res.json())
    .then(json => {
      genStatus = json.status
      let showLink = true
      let downloadURL = self.state.downloadURL + self.state.timeStamp
    	self.setState({genStatus, showLink, showReport, downloadURL});
    });
  }

  getReport() {
    let self = this;
    fetch(API_URL + 'report/' + self.state.timeStamp)
    .then(res => res.json())
    .then(json => {
      let report = json.data
      let showReport = true
    	self.setState({report, showReport});
    });
  }

  render() {
    return (
      <div>
        <div>
          <button className="App-button" disabled={this.state.genStatus === 'Loading...'} onClick={this.generateString}>Generate</button>
        </div>
        <p>
          <span>{this.state.genStatus}</span>
        </p>
        { this.state.showLink ? 
        <div>
          <a className="App-link" href={this.state.downloadURL}>{this.state.downloadURL}</a>
          <p>
            <button className="App-button" onClick={this.getReport}>Report</button>
          </p>
        </div> 
        : null }
        { this.state.showReport ? 
        <div>
          <p>Alphabetical: {this.state.report.alphabetical}</p>
          <p>Real Number: {this.state.report.real_number}</p>
          <p>Integer: {this.state.report.integer}</p>
          <p>Alphanumeric: {this.state.report.alphanumeric}</p>
        </div> 
        : null }
      </div>
    );
  }
}

export default StringGen;