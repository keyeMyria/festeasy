import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Button, Menu, Container, Header } from 'semantic-react'
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
        <button id="open-cart" className="ui basic button">
          <i id="open-cart" className="ui large cart icon" />
        </button>,
        <NavLink key="c" to="/account">Account</NavLink>,
        <Button key="b" onClick={this.context.signOut}>Sign Out</Button>,
      ]
    } else {
      links = [
        <NavLink key="c" to="/sign-in">Sign In</NavLink>,
        <NavLink key="d" to="/sign-up">Sign Up</NavLink>,
      ]
    }
    return (
      <Menu fixed secondary pointing>
        <Container>
          <Header item>
            <Link to="/">Home</Link>
          </Header>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/festivals">Festivals</NavLink>
          <NavLink to="/store">Store</NavLink>
          <NavLink to="/panels">Panel Test</NavLink>
          <div className="right menu">
            {links}
          </Menu>
        </Container>
      </Menu>
    )
  }
}
