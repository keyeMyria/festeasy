import React, { PropTypes, Component } from 'react'
import NavLink from 'common/navLink.jsx'
import PageMenu from 'admin/utils/pageMenu.jsx'


export default function(links) {
  return class extends Component {
    static propTypes = {
      children: PropTypes.any.isRequired,
    }

    render() {
      return (
        <div>
          {links ?
            <PageMenu>
              {links.map((link) => (
                <NavLink
                  key={link.url}
                  to={link.url}
                >
                  {link.text}
                </NavLink>
              ))}
            </PageMenu>
          : ''}
          <br />
          {this.props.children}
        </div>
      )
    }
  }
}
