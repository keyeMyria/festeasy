import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'


class Review extends React.Component {
  render() {
    const { cart, onProceed } = this.props
    const festival = cart.festival
    return (
      <div>
        <h2 className="ui header">Review Cart</h2>
        <div>
          <p>Festival: {festival.name}</p>
        </div>
        <table className="ui table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sub Total</th>
            </tr>
          </thead>
          <tbody>
            {cart.cart_products.map((cp) => (
              <tr key={cp.id}>
                <td>{cp.product.name}</td>
                <td>{cp.quantity}</td>
                <td>{cp.sub_total_rands}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <Button onClick={onProceed}>Proceed</Button>
      </div>
    )
  }
}

Review.propTypes = {
  cart: PropTypes.object.isRequired,
  onProceed: PropTypes.func.isRequired,
}


export default class ReviewContainer extends React.Component {
  constructor() {
    super()
    this.onProceed = this.onProceed.bind(this)
  }

  onProceed() {
    this.context.router.push('/checkout/payment')
  }

  render() {
    const { cart } = this.context
    return (
      <div>
        <Review
          cart={cart}
          onProceed={this.onProceed}
        />
      </div>
    )
  }
}

ReviewContainer.contextTypes = {
  router: PropTypes.object.isRequired,
  cart: PropTypes.object.isRequired,
}
