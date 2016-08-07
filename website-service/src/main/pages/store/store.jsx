import React, { PropTypes } from 'react'
import { Link } from 'react-router'


export default class Store extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        <h1 className="ui center aligned header">Store</h1>
        <div className="ui divider" />
        <div className="ui grid">
          <div className="four wide column">
            <h4 className="ui header">Product Categories</h4>
            <div className="ui vertical pointing menu">
              <Link className="item" activeClassName="active" to="/store">All</Link>
              <div className="item">
                <b>Alcohol</b>
                <div className="menu">
                  <a className="item">Beer</a>
                  <a className="item">Wine</a>
                </div>
              </div>
              <div className="item">
                <b>Food</b>
                <div className="menu">
                  <a className="item">Snacks</a>
                  <a className="item">Meals</a>
                </div>
              </div>
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
