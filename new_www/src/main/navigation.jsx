import React from 'react';
import { Link } from 'react-router'


const NavLink = React.createClass({
  render: function() {
    return (
        <Link {...this.props} className="item" activeClassName="active"/>
    )
  }
})


const Navigation = React.createClass({
  render: function() {
    return (
      <div className="ui fixed menu">
        <div className="ui container">
          <div className="header item">
            <Link to="/">Home</Link>
          </div>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/festivals">Festivals</NavLink>
          <NavLink to="/store">Store</NavLink>
        </div>
      </div>
    )
  }
})


module.exports = Navigation
