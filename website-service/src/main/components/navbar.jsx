import React, { PropTypes } from 'react'
import { Button, Menu, Container } from 'semantic-react'
import NavLink from 'common/navLink.jsx'


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
        <button key="d" id="open-cart" className="ui basic button">
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
      // TODO: Use secondary, but its broken.
      <Menu pointing inverted>
        <Container>
          <NavLink to="/" onlyActiveOnIndex>HOME</NavLink>
          <NavLink to="/festivals">FESTIVALS</NavLink>
          <NavLink to="/store">STORE</NavLink>
          <NavLink to="/about">ABOUT</NavLink>
          <Menu floated="right">
            {links}
          </Menu>
        </Container>
      </Menu>
    )
  }
}
