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
      links = (
        <Menu floated="right">
          <NavLink to="/cart">CART</NavLink>
          <NavLink to="/account">ACCOUNT</NavLink>
          <Button onClick={this.context.signOut}>Sign Out</Button>
        </Menu>
      )
    } else {
      links = (
        <Menu floated="right">
          <NavLink to="/sign-in">SIGN IN</NavLink>
          <NavLink to="/sign-up">SIGN UP</NavLink>
        </Menu>
      )
    }
    return (
      // TODO: Use secondary, but its broken.
      <Menu pointing inverted>
        <Container>
          <NavLink to="/" onlyActiveOnIndex>HOME</NavLink>
          <NavLink to="/festivals">FESTIVALS</NavLink>
          <NavLink to="/store">STORE</NavLink>
          <NavLink to="/about">ABOUT</NavLink>
          <NavLink to="/how-it-works">HOW IT WORKS</NavLink>
          {links}
        </Container>
      </Menu>
    )
  }
}
