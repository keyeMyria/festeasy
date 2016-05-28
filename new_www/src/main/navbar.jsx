import React from 'react';
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
        </div>
      </div>
    )
  }
}
