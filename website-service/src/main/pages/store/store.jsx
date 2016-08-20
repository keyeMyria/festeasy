import React, { PropTypes } from 'react'


export default class Store extends React.Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    children: PropTypes.any.isRequired,
    location: PropTypes.object.isRequired,
  }

  render() {
    return (
      <div>
        <div className="ui container">
          {this.props.children}
        </div>
      </div>
    )
  }
}
