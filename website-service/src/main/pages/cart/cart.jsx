import React from 'react'
import Cart from 'main/components/myCart.jsx'
import CartContainer from 'main/components/cart/cartContainer.jsx'

export default class CartPage extends React.Component {
  render() {
    return (
      <div className="ui container">
        <CartContainer>
          <Cart />
        </CartContainer>
      </div>
    )
  }
}
