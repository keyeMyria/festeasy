import React, { PropTypes } from 'react'


export default class Festivals extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        <h1 className="ui center aligned header">Festivals</h1>
        <div className="ui divider" />
        {this.props.children}
      </div>
    )
  }
}
