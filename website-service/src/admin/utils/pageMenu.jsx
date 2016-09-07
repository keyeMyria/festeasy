import React, { PropTypes } from 'react'
import { Menu } from 'semantic-react'


export default class PageMenu extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        <Menu secondary pointing>
          {this.props.children}
        </Menu>
      </div>
    )
  }
}
