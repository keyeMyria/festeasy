import React, { PropTypes } from 'react'
import { connect } from 'react-refetch'


const cartProductType = PropTypes.shape({
  id: PropTypes.number.isRequired,
  'product_id': PropTypes.number.isRequired,
  product: PropTypes.object.isRequired
})


const cartType = PropTypes.shape({
  id: PropTypes.number.isRequired,
  total_rands: PropTypes.number.isRequired,
  festival: PropTypes.object,
  cart_products: PropTypes.oneOfType([
    PropTypes.array,
    cartProductType
  ]).isRequired
})


const CartProductListItem = React.createClass({
  propTypes: {
    cartProduct: cartProductType.isRequired
  },


  render: function() {
    const { cartProduct } = this.props
    return (
      <div>
        <p>{cartProduct.product.name}</p>
        <p>Price: {cartProduct.product.price_rands}</p>
        <p>Quantity: {cartProduct.quantity}</p>
        <hr />
      </div>
    )
  }
})


const CartProductList = React.createClass({
  propTypes: {
    cartProducts: PropTypes.arrayOf(
      cartProductType
    ).isRequired
  },


  render: function() {
    const { cartProducts } = this.props
    return (
      <div>
        {cartProducts.map(cartProduct => (
          <CartProductListItem key={cartProduct.id} cartProduct={cartProduct}/>
        ))}
      </div>
    )
  }
})


const Cart = React.createClass({
  propTypes: {
    cart: cartType.isRequired
  },


  render: function() {
    const { cart } = this.props
    return (
      <div>
        <h1>Cart</h1>
        <CartProductList cartProducts={cart.cart_products}/>
        <p>Total: {cart.total_rands}</p>
      </div>
    )
  }
})


const CartContainer = React.createClass({
  propTypes: {
    cartFetch: PropTypes.object.isRequired
  },


  render: function() {
    const { cartFetch } = this.props
    if (cartFetch.pending) {
      return <div>Loading...</div>
    } else if (cartFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Cart cart={cartFetch.value}/>
    }
  }
})


// TODO: Use authenticated user id.
export default connect(() => ({
  cartFetch: 'http://localhost:5000/api/v1/users/1/cart'
}))(CartContainer)
