import React from 'react';


const Festival = React.createClass({
  render: function() {
    return (
      <div>
        {this.props.festival.name}
      </div>
    )
  }
})


const FestivalContainer = React.createClass({
  getInitialState: function() {
    return {
      festival: {}
    };
  },


  componentDidMount: function() {
    this.serverRequest = $.get(`http://localhost:5000/api/v1/festivals/${this.props.params.festivalId}`, function(result) {
      this.setState({
        festival: result
      })
    }.bind(this))
  },


  componentWillUnmount: function() {
    this.serverRequest.abort();
  },


  render: function() {
    return (
      <Festival festival={this.state.festival}/>
    )
  }
})


module.exports = FestivalContainer
