import React from 'react';


const Store = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Store</h1>
      </div>
    )
  }
})


const StoreContainer = React.createClass({
  render: function() {
    return (
      <div>
        <Store />
      </div>
    )
  }
})


module.exports = StoreContainer
