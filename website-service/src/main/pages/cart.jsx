import React, { PropTypes } from 'react'
import { Button, Input, Option } from 'semantic-react'
import MySelect from 'utils/mySelect.jsx'
import Page from 'common/page.jsx'


class Cart extends React.Component {
  static propTypes = {
    cart: PropTypes.object.isRequired,
    festivals: PropTypes.array.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
    selectFestival: PropTypes.func.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    onCheckout: PropTypes.func.isRequired,
  }

  render() {
    const { cart, festivals, updateQuantity, onCheckout } = this.props
    const options = festivals.map((festival) => (
      <Option key={festival.id} value={festival.id}>{festival.name}</Option>
    ))
    return (
      <div>
        <MySelect
          fluid
          selected={[cart.festival_id]}
          updateSelected={(selected) => this.props.selectFestival(selected[0])}
          options={options}
        />
        <table className="ui table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sub Total</th>
              <th>Remove</th>
            </tr>
          </thead>
          <tbody>
            {cart.cart_products.map((cartProduct) => (
              <tr key={cartProduct.id}>
                <td>{cartProduct.product.name}</td>
                <td>
                  <Input
                    type="number"
                    onChange={(e) => updateQuantity(e, cartProduct)}
                    value={cartProduct.quantity}
                  />
                </td>
                <td>{cartProduct.sub_total_rands}</td>
                <td>
                  <button
                    className="ui button"
                    onClick={() => { this.props.removeCartProduct(cartProduct) }}
                  >
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>Total: R{cart.total_rands}</div>
        <Button onClick={onCheckout}>Secure Checkout</Button>
      </div>
    )
  }
}


export default class CartContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    router: PropTypes.object.isRequired,
    authDetails: PropTypes.object.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      cart: null,
      festivals: null,
      error: null,
    }
    this.onCheckout = this.onCheckout.bind(this)
    this.getCart = this.getCart.bind(this)
    this.removeCartProduct = this.removeCartProduct.bind(this)
    this.selectFestival = this.selectFestival.bind(this)
    this.updateQuantity = this.updateQuantity.bind(this)
  }

  componentDidMount() {
    this.getCart()
  }

  onCheckout() {
    this.context.router.push('/checkout/review')
  }

  getCart() {
    const { store, authDetails } = this.context
    store.ejectAll('cartProduct')
    const userFetch = store.find('user', authDetails.userId)
    const festivalsFetch = store.findAll('festival')
    userFetch.then((user) => {
      const cartFetch = store.find(
        'cart',
        user.id,
        { bypassCache: true }
      )
      Promise.all([cartFetch, festivalsFetch])
        .then((values) => {
          this.setState({
            cart: values[0],
            festivals: values[1],
          })
        })
        .catch(() => {
          this.setState({
            error: 'Something went wrong.',
          })
        })
    })
  }

  removeCartProduct(cp) {
    this.context.store.destroy('cartProduct', cp.id)
      .then(() => {
        this.getCart()
      })
  }

  updateQuantity(e, updatedCp) {
    this.state.cart.cart_products.forEach((cp) => {
      if (cp.id === updatedCp.id) {
        console.log('Update the quantity.')
      }
    })
  }

  selectFestival(festivalId) {
    this.context.store.update(
      'cart',
      this.state.cart.id,
      { festival_id: festivalId },
      { method: 'PATCH' }
    )
      .then(() => {
        this.getCart()
      })
  }

  render() {
    const { cart, error, festivals } = this.state
    return (
      <Page
        isLoading={!cart && !festivals && !error}
        contentError={error}
        content={
          cart && festivals ?
            <Cart
              cart={cart}
              festivals={festivals}
              removeCartProduct={this.removeCartProduct}
              selectFestival={this.selectFestival}
              updateQuantity={this.updateQuantity}
              onCheckout={this.onCheckout}
            /> : ''
        }
      />
    )
  }
}
