import React, { PropTypes } from 'react'
import NavLink from 'main/components/navLink.jsx'


export default class Account extends React.Component {
  static propTypes = {
    children: PropTypes.any,
  }

  render() {
    return (
      <div>
        <h1 className="ui center aligned header">Account</h1>
        <div className="ui divider" />
        <div className="ui two column grid">
          <div className="four wide column">
            <div className="ui vertical pointing menu">
              <NavLink to="/account/orders">Orders</NavLink>
              <NavLink to="/account/settings">Settings</NavLink>
            </div>
          </div>
          <div className="twelve wide column">
            {this.props.children}
          </div>
        </div>
      </div>
    )
  }
}
