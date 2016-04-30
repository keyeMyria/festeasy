import React from 'react';
import { Link } from 'react-router';


const Festival = React.createClass({
  render: function() {
    return (
      <div>
        <h2>
          <Link to={`/festivals/${this.props.festival.id}`}>
            {this.props.festival.name}
          </Link>
        </h2>
        <p>{this.props.festival.description}</p>
        <p>Starts: {this.props.festival.starts_on}</p>
        <p>Ends: {this.props.festival.ends_on}</p>
      </div>
    )
  }
})


const Festivals = React.createClass({
  render: function() {
    const festivalNodes = this.props.festivals.map(function(festival) {
      return (
        <div key={festival.id}>
          <Festival festival={festival}/>
        </div>
      )
    })
    return (
      <div>
        <h1>Festivals</h1>
        {festivalNodes}
      </div>
    )
  }
})


const FestivalsContainer = React.createClass({
  getInitialState: function() {
    return {
      festivals: []
    };
  },


  componentDidMount: function() {
    this.serverRequest = $.get('http://localhost:5000/api/v1/festivals', function(result) {
      this.setState({
        festivals: result
      })
    }.bind(this))
  },


  componentWillUnmount: function() {
    this.serverRequest.abort();
  },


  render: function() {
    return (
      <Festivals festivals={this.state.festivals} />
    )
  }
})


module.exports = FestivalsContainer
