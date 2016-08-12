import React from 'react'
import Cart from 'main/myCart.jsx'
import CartContainer from '../cartContainer.jsx'

export default class CartPage extends React.Component {
  render() {
    return (
      <div>
        <CartContainer>
          <Cart />
        </CartContainer>
      </div>
    )
  }
}
