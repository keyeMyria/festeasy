import React, { PropTypes } from 'react'
import { jsonApiRequest } from '../utils/request.jsx'
import getAuthDetails from '../utils/auth.jsx'


const Cart = React.createClass({
  propTypes: {
    cart: PropTypes.shape({
      id: PropTypes.number.isRequired
    })
  },


  render: function() {
    return (
      <div>
        <h1>Cart</h1>
      </div>
    )
  }
})


const CartContainer = React.createClass({
  getInitialState: function() {
    return {
      cart: {}
    };
  },


  componentDidMount: function() {
    const it = this
    const userId = getAuthDetails
    const request = jsonApiRequest('GET', '/users/1/cart')
    request.then(function(response) {
      return response.json()
    }).then(function(json) {
      console.log(json)
      it.setState({
        cart: json
      })
    })
  },


  componentWillUnmount: function() {
    this.serverRequest.abort();
  },


  render: function() {
    return (
      <Cart cart={this.state.cart} />
    )
  }
})


module.exports = CartContainer
