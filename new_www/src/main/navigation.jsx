import React, { PropTypes } from 'react';
import { Link } from 'react-router'
import auth from '../utils/auth.jsx'


const NavLink = React.createClass({
  render: function() {
    return (
        <Link {...this.props} className="item" activeClassName="active"/>
    )
  }
})


const Navigation = React.createClass({
  contextTypes: {
    isSignedIn: PropTypes.bool.isRequired
  },


  _handleClick: function() {
    auth.signOut()
  },


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
          <NavLink to="/cart">Cart</NavLink>
          <NavLink to="/sign-in">Sign In</NavLink>
          <button onClick={this._handleClick} className="ui botton">Sign Out</button>
        </div>
      </div>
    )
  }
})


module.exports = Navigation
