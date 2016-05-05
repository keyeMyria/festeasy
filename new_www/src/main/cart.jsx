import React, { PropTypes } from 'react'
import { connect } from 'react-refetch'
import { cartProductShape, cartShape } from '../utils/shapes.jsx'


const CartProductListItem = React.createClass({
  propTypes: {
    cartProduct: cartProductShape.isRequired,
    updateQuantity: PropTypes.func.isRequired,
  },

  getInitialState: function() {
    return { quantity: this.props.cartProduct.quantity }
  },

  handleChange: function(event) {
    this.setState({ quantity: event.target.value });
  },

  updateQuantity: function() {
    this.props.updateQuantity({
      id: this.props.cartProduct.id,
      quantity: this.state.quantity,
    })
  },

  render: function() {
    const { cartProduct } = this.props
    return (
      <div>
        <p>{cartProduct.product.name}</p>
        <p>Price: {cartProduct.product.price_rands}</p>
        <p>
          <input type="number" value={this.state.quantity} onChange={this.handleChange} />
        </p>
        <button onClick={this.updateQuantity}>Update</button>
        <hr />
      </div>
    )
  },
})


const CartProductList = React.createClass({
  propTypes: {
    updateQuantity: PropTypes.func.isRequired,
    cartProducts: PropTypes.arrayOf(
      cartProductShape
    ).isRequired,
  },

  render: function() {
    const { cartProducts, updateQuantity } = this.props
    return (
      <div>
        {cartProducts.map(cartProduct => (
          <CartProductListItem
            key={cartProduct.id}
            updateQuantity={updateQuantity}
            cartProduct={cartProduct}
          />
        ))}
      </div>
    )
  },
})


const Cart = React.createClass({
  propTypes: {
    updateQuantity: PropTypes.func.isRequired,
    cart: cartShape.isRequired,
  },

  render: function() {
    const { cart, updateQuantity } = this.props
    return (
      <div>
        <h1>Cart</h1>
        <CartProductList
          updateQuantity={updateQuantity}
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
    updateQuantity: PropTypes.func.isRequired,
  },

  contextTypes: {
    authUserId: PropTypes.number.isRequired,
    apiPrefix: PropTypes.string.isRequired,
  },

  render: function() {
    const { cartFetch, updateQuantity } = this.props
    if (cartFetch.pending) {
      return <div>Loading...</div>
    } else if (cartFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Cart updateQuantity={updateQuantity} cart={cartFetch.value} />
    }
  },
})


export default connect((props, context) => {
  const cartUrl = `${context.apiPrefix}/v1/users/${context.authUserId}/cart`
  return {
    cartFetch: cartUrl,
    updateQuantity: ({ id, quantity }) => ({
      meh: {
        url: `${context.apiPrefix}/v1/cart-products/${id}`,
        method: 'PATCH',
        body: JSON.stringify({
          quantity: quantity,
        }),
        andThen: () => ({
          cartFetch: {
            url: cartUrl,
            force: true,
          },
        }),
      },
    }),
  }
})(CartContainer)
