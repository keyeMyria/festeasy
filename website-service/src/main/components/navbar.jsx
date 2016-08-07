import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import NavLink from 'main/components/navLink.jsx'


export default class Navbar extends React.Component {
  static contextTypes = {
    authDetails: PropTypes.object,
    signOut: PropTypes.func.isRequired,
  }

  render() {
    let links = []
    if (this.context.authDetails) {
      links = [
        <NavLink key="a" to="/cart">Cart</NavLink>,
        <NavLink key="c" to="/account">Account</NavLink>,
        <button key="b" className="ui button" onClick={this.context.signOut}>Sign Out</button>,
      ]
    } else {
      links = [
        <NavLink key="c" to="/sign-in">Sign In</NavLink>,
        <NavLink key="d" to="/sign-up">Sign Up</NavLink>,
      ]
    }
    return (
      <div className="ui fixed secondary pointing menu">
        <div className="ui container">
          <div className="header item">
            <Link to="/">Home</Link>
          </div>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/festivals">Festivals</NavLink>
          <NavLink to="/store">Store</NavLink>
          <div className="right menu">
            {links}
          </div>
        </div>
      </div>
    )
  }
}
