import React from 'react';
import Navigation from './navigation.jsx'


const Main = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Main</h1>
        <h1>Main</h1>
        <h1>Main</h1>
        <Navigation />
        {this.props.children}
      </div>
    )
  }
})


module.exports = Main
