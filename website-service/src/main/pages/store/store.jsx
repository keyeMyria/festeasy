import React, { PropTypes } from 'react'
import NavLink from 'common/navLink.jsx'


export default class Store extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        <div className="ui container">
          <div className="ui two column grid">
            <div className="four wide column">
              <div className="ui vertical pointing menu">
                <NavLink to="/store/categories/alchohol">Alchohol</NavLink>
                <NavLink to="/store/categories/food">Food</NavLink>
              </div>
            </div>
            <div className="twelve wide column">
              {this.props.children}
            </div>
          </div>
        </div>
      </div>
    )
  }
}
