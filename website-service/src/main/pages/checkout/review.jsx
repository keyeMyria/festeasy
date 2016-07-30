import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'
import Page from 'common/page.jsx'


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
  static contextTypes = {
    router: PropTypes.object.isRequired,
    store: PropTypes.object.isRequired,
    authDetails: PropTypes.object.isRequired,
    axios: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
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
    const { axios } = this.context
    const cartId = this.state.cart.id
    axios.request({
      method: 'post',
      url: `carts/${cartId}/checkout`,
    })
      .then((response) => {
        const invoiceId = response.data.current_invoice.id
        this.context.router.push(`/checkout/payment?invoice-id=${invoiceId}`)
      })
  }

  getCart() {
    const { store, authDetails } = this.context
    store.find('user', authDetails.userId)
      .then((user) => {
        store.find(
          'cart',
          user.id,
          { bypassCache: true }
        )
          .then((cart) => {
            this.setState({
              cart,
            })
          })
      })
  }

  render() {
    const { cart, error } = this.state
    return (
      <Page
        isLoading={!cart && !error}
        content={
          cart ? <Review cart={cart} onProceed={this.onProceed} /> : ''
        }
      />
    )
  }
}
