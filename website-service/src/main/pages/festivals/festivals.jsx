import React, { PropTypes } from 'react'


export default class Festivals extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
}
