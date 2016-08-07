import React, { PropTypes } from 'react'
import CartPanel from './cartPanel.jsx'
import CartItem from './cartItem.jsx'

export default class Panel extends React.Component {
  render() {
    return (
      <div>
        <CartPanel >
					<CartItem />
					<CartItem />
					<CartItem />
					<CartItem />
        </CartPanel>
      </div>
    )
  }
}
