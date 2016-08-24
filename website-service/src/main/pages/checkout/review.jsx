import React, { PropTypes } from 'react'
import {
  Form,
  Field,
  Input,
  Grid,
  Column,
  Button,
  Table,
  Tr,
  Td,
  Header,
  Image,
} from 'semantic-react'
import Page from 'utils/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'
import apiEndpoint from 'apiEndpoint.js'


class DeliveryForm extends React.Component {
  static propTypes = {
    onSubmit: PropTypes.func.isRequired,
    isSubmitting: PropTypes.bool.isRequired,
  }

  constructor() {
    super()
    this.state = {
      streetAddress: '',
      suburb: '',
      city: '',
    }
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  onChange(e) {
    const state = {}
    state[e.target.name] = e.target.value
    this.setState(state)
  }

  onSubmit(e) {
    e.preventDefault()
    this.props.onSubmit(this.state)
  }

  render() {
    const { streetAddress, suburb, city } = this.state
    const { isSubmitting } = this.props
    return (
      <Form onSubmit={this.onSubmit}>
        <Field label="Street Address" required>
          <Input
            onChange={this.onChange}
            value={streetAddress}
            name="streetAddress"
            placeholder="22 Stellenberg Avenue"
            required
          />
        </Field>
        <Field label="Suburb" required>
          <Input
            onChange={this.onChange}
            value={suburb}
            name="suburb"
            placeholder="Kenilworth"
            required
          />
        </Field>
        <Field label="City" required>
          <Input
            onChange={this.onChange}
            value={city}
            name="city"
            placeholder="Cape Town"
            required
          />
        </Field>
        <Button color="green" state={isSubmitting ? 'loading' : ''}>Proceed</Button>
      </Form>
    )
  }
}


class Review extends React.Component {
  static propTypes = {
    cart: PropTypes.object.isRequired,
    cartProducts: PropTypes.array.isRequired,
    onSubmit: PropTypes.func.isRequired,
    isSubmitting: PropTypes.bool.isRequired,
  }

  render() {
    const { cart, cartProducts, onSubmit, isSubmitting } = this.props
    const festival = cart.festival
    const imageHeight = 40
    return (
      <div>
        <Header emphasis="dividing">1. Review your cart for {festival.name}</Header>
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
                <Td>
                  <Grid columns={2}>
                    <Column width={3}>
                      {cp.product.thumbnail_image_id ?
                        <Image
                          centered
                          style={{ maxHeight: imageHeight, width: 'auto', height: 'auto' }}
                          alt="product thumbnail"
                          src={apiEndpoint.concat(
                            `v1/images/${cp.product.thumbnail_image_id}/image?height=${imageHeight}`
                          )}
                        /> : 'No thumbnail image'
                      }
                    </Column>
                    <Column>
                      {cp.product.name}
                    </Column>
                  </Grid>
                </Td>
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
        <div className="ui right aligned container" style={{ fontSize: 18 }}>
          Total: <PriceFormatter rands={cart.total_rands} />
        </div>
        <Header emphasis="dividing">2. Enter your Delivery Address</Header>
        <Grid>
          <Column width={5}>
            <DeliveryForm onSubmit={onSubmit} isSubmitting={isSubmitting} />
          </Column>
        </Grid>
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
      isSubmitting: false,
    }
    this.onProceed = this.onProceed.bind(this)
    this.fetchCart = this.fetchCart.bind(this)
    this.fetchCartProducts = this.fetchCartProducts.bind(this)
  }

  componentDidMount() {
    this.fetchCart()
    this.fetchCartProducts()
  }

  onProceed(addressData) {
    this.setState({ isSubmitting: true })
    const a = addressData
    const { axios } = this.context
    const cartId = this.state.cart.id
    axios({
      method: 'post',
      url: `v1/carts/${cartId}/checkout`,
      data: {
        shipping_address: `${a.streetAddress}, ${a.suburb}, ${a.city}`,
      },
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
    const { cart, cartProducts, error, isSubmitting } = this.state
    const isReady = cart && cartProducts
    return (
      <Page
        isLoading={!isReady && !error}
        content={
          isReady ?
            <Review
              cart={cart}
              cartProducts={cartProducts}
              onSubmit={this.onProceed}
              isSubmitting={isSubmitting}
            />
          : ''
        }
      />
    )
  }
}
