import React, { PropTypes } from 'react'


export default class AuthBox extends React.Component {
  static propTypes = {
    title: PropTypes.any.isRequired,
    children: PropTypes.any.isRequired,
  }

  render() {
    const { title, children } = this.props
    return (
      <div className="ui container centered grid">
        <div className="ui segment six wide column">
          <h1 className="ui header">{title}</h1>
          {children}
        </div>
      </div>
    )
  }
}
