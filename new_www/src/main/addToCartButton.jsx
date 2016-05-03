import React, { PropTypes } from 'react';
import 'whatwg-fetch';


const AddToCartButton = React.createClass({
  propTypes: {
    productId: PropTypes.number.isRequired
  },


  contextTypes: {
    apiPrefix: PropTypes.string.isRequired,
    authUserId: PropTypes.number.isRequired
  },


  _handleClick: function() {
    const { apiPrefix, authUserId } = this.context
    fetch(`${apiPrefix}/v1/users/${authUserId}/cart/cart-products`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'product_id': this.props.productId,
        'cart_id': 1
      })
    })
  },


  render: function() {
    return (
      <div>
        <button onClick={this._handleClick} className="ui button">Add to cart</button>
      </div>
    )
  }
})


module.exports = AddToCartButton
