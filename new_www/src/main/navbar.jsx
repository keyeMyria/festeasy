import React, { PropTypes } from 'react';
import { Link } from 'react-router'


class NavLink extends React.Component {
  render() {
    return (
      <Link
        {...this.props}
        className="item"
        activeClassName="active"
      />
    )
  }
}

export default class Navbar extends React.Component {
  render() {
    let links = []
    if (this.context.authSession) {
      links = [
        <NavLink key="a" to="/cart">Cart</NavLink>,
        <button key="b" className="ui button" onClick={this.context.signOut}>Sign Out</button>,
      ]
    } else {
      links = [
        <NavLink key="c" to="/sign-in">Sign In</NavLink>,
      ]
    }
    return (
      <div className="ui fixed menu">
        <div className="ui container">
          <div className="header item">
            <Link to="/">Home</Link>
          </div>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/festivals">Festivals</NavLink>
          <NavLink to="/store">Store</NavLink>
          {links}
        </div>
      </div>
    )
  }
}

Navbar.contextTypes = {
  authSession: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
  signOut: PropTypes.func.isRequired,
}
