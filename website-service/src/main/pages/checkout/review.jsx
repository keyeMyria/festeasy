import React, { PropTypes } from 'react'
import { Button, Table, Tr, Td, Header } from 'semantic-react'
import Page from 'utils/page.jsx'
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
        <Header>Review Cart</Header>
        <p>Festival: {festival.name}</p>
        <Table>
          <thead>
            <Tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Unit Price</th>
              <th>Sub Total</th>
            </Tr>
          </thead>
          <tbody>
            {cartProducts.map((cp) => (
              <Tr key={cp.id}>
                <Td>{cp.product.name}</Td>
                <Td>{cp.quantity}</Td>
                <Td>
                  <PriceFormatter rands={cp.product.price_rands} />
                </Td>
                <Td>
                  <PriceFormatter rands={cp.sub_total_rands} />
                </Td>
              </Tr>
            ))}
          </tbody>
        </Table>
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
    axios({
      method: 'post',
      url: `v1/carts/${cartId}/checkout`,
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
