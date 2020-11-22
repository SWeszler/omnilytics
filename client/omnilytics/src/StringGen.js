import { Component } from 'react';
import './App.css';

class StringGen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      myString: 'hello...'
    }
  }

  generateString() {
    fetch('http://localhost:5000/')
		.then(res => res.json())
		.then(json => {
			const myString = json.sequence;
			this.setState({myString});
		});
  }

  render() {
    return (
      <div>
        <div>
          <button onClick={this.generateString}>Generate</button>
        </div>
        <div>
          <span>{this.state.myString}</span>
        </div>
      </div>
    );
  }
}

export default StringGen;