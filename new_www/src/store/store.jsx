import React from 'react';
import Navigation from './navigation.jsx'


const Store = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Store</h1>
        <Navigation />
        {this.props.children}
      </div>
    )
  }
})


module.exports = Store
