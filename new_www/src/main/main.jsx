import React from 'react';
import Navigation from './navigation.jsx'


const Main = React.createClass({
  render: function() {
    return (
      <div style={{paddingTop: 55}}>
        <Navigation />
        <div className="ui container">
          {this.props.children}
        </div>
      </div>
    )
  }
})


module.exports = Main
