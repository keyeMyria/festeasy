import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Menu, Container, Header } from 'semantic-react'
import NavLink from 'common/navLink.jsx'


export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }

  render() {
    return (
      <div>
        <Menu pointing>
          <Container>
            <Header item>
              <Link to="/admin">Admin Home</Link>
            </Header>
            <NavLink to="/admin/stock">Stock</NavLink>
          </Container>
        </Menu>
        <Container>
          {this.props.children}
        </Container>
      </div>
    )
  }
}
