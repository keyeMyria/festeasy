import React, { PropTypes } from 'react'
import getAuthDetails from '../utils/auth.jsx'
import { connect, PromiseState } from 'react-refetch'


const cartType = PropTypes.shape({
  id: PropTypes.number.isRequired,
  total_rands: PropTypes.number.isRequired,
  festival: PropTypes.object,
  cart_products: PropTypes.array
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
        <p>Total: {cart.total_rands}</p>
      </div>
    )
  }
})


const CartContainer = React.createClass({
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


export default connect(props => ({
  cartFetch: 'http://localhost:5000/api/v1/users/1/cart'
}))(CartContainer)
