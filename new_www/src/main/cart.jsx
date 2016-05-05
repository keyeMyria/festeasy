import React, { PropTypes } from 'react'
import { connect } from 'react-refetch'
import { cartProductShape, cartShape } from '../utils/shapes.jsx'


const CartProductListItem = React.createClass({
  propTypes: {
    cartProductUpdate: PropTypes.func.isRequired,
    cartProduct: cartProductShape.isRequired,
  },

  handleChange: function(event) {
    const cartProduct = this.props.cartProduct
    cartProduct.quantity = event.target.value
    this.props.cartProductUpdate(cartProduct)
  },

  render: function() {
    const { cartProduct } = this.props
    return (
      <div>
        <p>{cartProduct.product.name}</p>
        <p>Price: {cartProduct.product.price_rands}</p>
        <p>
          <input type="number" value={cartProduct.quantity} onChange={this.handleChange} />
        </p>
        <hr />
      </div>
    )
  },
})


const CartProductList = React.createClass({
  propTypes: {
    cartProductUpdate: PropTypes.func.isRequired,
    cartProducts: PropTypes.arrayOf(
      cartProductShape
    ).isRequired,
  },

  render: function() {
    const { cartProducts, cartProductUpdate } = this.props
    return (
      <div>
        {cartProducts.map(cartProduct => (
          <CartProductListItem
            key={cartProduct.id}
            cartProductUpdate={cartProductUpdate}
            cartProduct={cartProduct}
          />
        ))}
      </div>
    )
  },
})


const Cart = React.createClass({
  propTypes: {
    cart: cartShape.isRequired,
  },

  getInitialState() {
    return {
      cart: this.props.cart,
    }
  },

  cartProductUpdate: function(cartProduct) {
    const cart = this.state.cart
    cart.cart_products.forEach((cp) => {
      if (cp.id === cartProduct.id) {
        cp.quantity = cartProduct.quantity
      }
      this.setState({
        cart: cart,
      })
    })
  },

  render: function() {
    const { cart } = this.state
    return (
      <div>
        <h1>Cart</h1>
        <CartProductList
          cartProductUpdate={this.cartProductUpdate}
          cartProducts={cart.cart_products}
        />
        <p>Total: {cart.total_rands}</p>
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
