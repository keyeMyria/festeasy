import React, { PropTypes } from 'react'
import update from 'react-addons-update'
import { connect } from 'react-refetch'
import { cartShape } from '../utils/shapes.jsx'

const Cart = React.createClass({
  propTypes: {
    cart: cartShape.isRequired,
  },

  getInitialState() {
    return {
      cart: this.props.cart,
    }
  },

  updateCart: function() {
    console.log('hi')
  },

  updateCartSubTotal: function() {
    let temp = 0
    this.state.cart.cart_products.forEach((cp) => {
      temp = temp + cp.sub_total_rands
    })
    this.state.cart.total_rands = temp
  },

  handleQuantityChange: function(id, event) {
    const newCartProducts = []
    this.state.cart.cart_products.forEach((cp) => {
      if (cp.id === id) {
        cp.sub_total_rands = parseInt(event.target.value, 10) * cp.product.price_rands
        this.updateCartSubTotal()
        newCartProducts.push(
          update(cp, { $merge: { 'quantity': parseInt(event.target.value, 10) } })
        )
      } else {
        newCartProducts.push(cp)
      }
    })
    this.setState({
      cart: update(this.state.cart, { $merge: { 'cart_products': newCartProducts } })
    })
  },

  render: function() {
    const { cart } = this.state
    return (
      <div>
        <h1>Cart</h1>
        <table className="ui sortable celled table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Unit Price</th>
              <th>Quantity</th>
              <th>Sub Total</th>
            </tr>
          </thead>
          <tbody>
            {this.state.cart.cart_products.map(cartProduct => (
              <tr key={cartProduct.id}>
                <td>{cartProduct.product.name}</td>
                <td>{cartProduct.product.price_rands}</td>
                <td>
                  <input
                    onChange={this.handleQuantityChange.bind(this, cartProduct.id)}
                    value={cartProduct.quantity}
                  />
                </td>
                <td>{cartProduct.sub_total_rands}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p>Total: {cart.total_rands}</p>
        <button className="ui button" onClick={this.updateCart}>Update</button>
      </div>
    )
  },
})


const CartContainer = React.createClass({
  propTypes: {
    cartFetch: PropTypes.object.isRequired,
  },

  contextTypes: {
    authUserId: PropTypes.number.isRequired,
    apiPrefix: PropTypes.string.isRequired,
  },

  render: function() {
    const { cartFetch } = this.props
    if (cartFetch.pending) {
      return <div>Loading...</div>
    } else if (cartFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Cart cart={cartFetch.value} />
    }
  },
})


export default connect((props, context) => {
  const cartUrl = `${context.apiPrefix}/v1/users/${context.authUserId}/cart`
  return {
    cartFetch: cartUrl,
  }
})(CartContainer)
