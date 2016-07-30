import React, { PropTypes } from 'react'
import { Link } from 'react-router'


export default class Account extends React.Component {
  static propTypes = {
    children: PropTypes.any,
  }

  render() {
    return (
      <div>
        <h1 className="ui header">Account</h1>
        <div className="ui two column grid">
          <div className="four wide column">
            <div className="ui vertical pointing menu">
              <Link className="item" to="/account/orders" activeClassName="active">Orders</Link>
              <Link className="item" to="/account/settings" activeClassName="active">Settings</Link>
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
