import React, { PropTypes } from 'react'
import axios from 'axios'
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
    this.state = {
      loading: true,
      cart: null,
      error: null,
    }
    this.onProceed = this.onProceed.bind(this)
    this.getCart = this.getCart.bind(this)
  }

  componentDidMount() {
    this.getCart()
  }

  onProceed() {
    const cartId = this.state.cart.id
    axios({
      method: 'post',
      url: `http://localhost:5000/api/v1/carts/${cartId}/checkout`,
    })
    .then((response) => {
      const invoiceId = response.data.current_invoice.id
      this.context.router.push(`/checkout/payment?invoice-id=${invoiceId}`)
    })
  }

  getCart() {
    this.setState({ loading: true })
    this.context.store.find(
      'cart',
      this.context.authUser.cart_id,
      {
        bypassCache: true,
      }
    )
    .then((cart) => {
      this.setState({
        loading: false,
        cart,
      })
    })
  }

  render() {
    const { cart, error } = this.state
    if (cart) {
      return (
        <Review
          cart={cart}
          onProceed={this.onProceed}
        />
      )
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading</div>
    }
  }
}

ReviewContainer.contextTypes = {
  router: PropTypes.object.isRequired,
  store: PropTypes.object.isRequired,
  authUser: PropTypes.object.isRequired,
}
