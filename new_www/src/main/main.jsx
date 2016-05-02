import React, { PropTypes } from 'react';
import Navigation from './navigation.jsx'


const Main = React.createClass({
  propTypes: {
    children: PropTypes.object.isRequired
  },


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
