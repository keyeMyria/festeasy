import React, { PropTypes } from 'react'
import { Menu } from 'semantic-react'
import NavLink from 'common/navLink.jsx'


export default class Stock extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }

  render() {
    return (
      <div>
        <Menu secondary pointing>
          <NavLink to="/admin/stock/list">List</NavLink>
          <NavLink to="/admin/stock/create">Create</NavLink>
        </Menu>
        {this.props.children}
      </div>
    )
  }
}
