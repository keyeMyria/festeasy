import React, { PropTypes } from 'react'


export default class Checkout extends React.Component {
  render() {
    return (
      <div>
        Checkout here
        {this.props.children}
      </div>
    )
  }
}

Checkout.propTypes = {
  children: PropTypes.any.isRequired,
}
