import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'
import Page from 'common/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


class Review extends React.Component {
  static propTypes = {
    cart: PropTypes.object.isRequired,
    cartProducts: PropTypes.array.isRequired,
    onProceed: PropTypes.func.isRequired,
  }

  render() {
    const { cart, cartProducts, onProceed } = this.props
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
            {cartProducts.map((cp) => (
              <tr key={cp.id}>
                <td>{cp.product.name}</td>
                <td>{cp.quantity}</td>
                <td>{cp.sub_total_rands}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>
          Total: <PriceFormatter rands={cart.total_rands} />
        </div>
        <Button onClick={onProceed}>Proceed</Button>
      </div>
    )
  }
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
      cartProducts: null,
      error: null,
    }
    this.onProceed = this.onProceed.bind(this)
    this.fetchCart = this.fetchCart.bind(this)
    this.fetchCartProducts = this.fetchCartProducts.bind(this)
  }

  componentDidMount() {
    this.fetchCart()
    this.fetchCartProducts()
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

  fetchCart() {
    const { store, authDetails } = this.context
    store.find('user', authDetails.userId)
      .then((user) => {
        store.find(
          'cart',
          user.cart_id,
          { bypassCache: true }
        )
          .then((cart) => {
            this.setState({
              cart,
            })
          })
      })
  }

  fetchCartProducts() {
    const { store, authDetails } = this.context
    store.find('user', authDetails.userId)
      .then((user) => {
        store.findAll(
          'cartProduct',
          { 'cart-id': user.cart_id },
          { bypassCache: true }
        )
          .then((cartProducts) => {
            this.setState({
              cartProducts,
            })
          })
      })
  }

  render() {
    const { cart, cartProducts, error } = this.state
    const isReady = cart && cartProducts
    return (
      <Page
        isLoading={!isReady && !error}
        content={
          isReady ?
            <Review
              cart={cart}
              cartProducts={cartProducts}
              onProceed={this.onProceed}
            />
          : ''
        }
      />
    )
  }
}
