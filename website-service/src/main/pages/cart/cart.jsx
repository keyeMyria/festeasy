import React, { PropTypes } from 'react'
import Page from 'utils/page.jsx'
import Cart from 'main/components/myCart.jsx'


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
      cartProducts: null,
      festivals: null,
      error: null,
    }
    this.fetchCart = this.fetchCart.bind(this)
    this.fetchFestivals = this.fetchFestivals.bind(this)
    this.fetchCartProducts = this.fetchCartProducts.bind(this)
    this.selectFestival = this.selectFestival.bind(this)
    this.updateQuantity = this.updateQuantity.bind(this)
    this.removeCartProduct = this.removeCartProduct.bind(this)
    this.onCheckout = this.onCheckout.bind(this)
  }

  componentWillMount() {
    this.fetchCart()
    this.fetchFestivals()
    this.fetchCartProducts()
  }

  onCheckout() {
    this.context.router.push('/checkout/review')
  }

  fetchFestivals() {
    const { store } = this.context
    return new Promise((resolve, reject) => {
      store.findAll('festival', { checkoutable: true })
        .then((festivals) => {
          this.setState({
            festivals,
          }, resolve(festivals))
        })
        .catch((error) => {
          this.setState({
            error: 'Something went wrong',
          }, reject(error))
        })
    })
  }

  fetchCartProducts() {
    const { store, authDetails } = this.context
    store.find('user', authDetails.userId)
      .then((user) => {
        store.findAll('cartProduct', { 'cart-id': user.cart_id }, { bypassCache: true })
          .then((cartProducts) => {
            this.setState({ cartProducts })
          })
          .catch(() => {
            this.setState({
              error: 'Something went wrong',
            })
          })
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  fetchCart() {
    return new Promise((resolve, reject) => {
      const { store, authDetails } = this.context
      store.find('user', authDetails.userId)
        .then((user) => {
          store.find('cart', user.cart_id, { bypassCache: true })
            .then((cart) => {
              this.setState({
                cart,
              }, resolve(cart))
            })
            .catch((error) => {
              this.setState({
                error: 'Something went wrong',
              }, reject(error))
            })
        })
        .catch((error) => {
          this.setState({
            error: 'Something went wrong',
          }, reject(error))
        })
    })
  }

  removeCartProduct(cp) {
    this.context.store.destroy('cartProduct', cp.id)
      .then(() => {
        this.fetchCart()
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  updateQuantity(cp, quantity) {
    const { store } = this.context
    store.update(
      'cartProduct',
      cp.id,
      { quantity: quantity },
      { method: 'patch' },
    )
      .then(() => {
        this.fetchCart()
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  selectFestival(festivalId) {
    const { store } = this.context
    return store.update(
      'cart',
      this.state.cart.id,
      { festival_id: festivalId },
      { method: 'PATCH' }
    )
      .then(() => (
        this.fetchCart()
      ))
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { cart, cartProducts, festivals, error } = this.state
    const isReady = cart && cartProducts && festivals
    return (
      <div>
        <h1 className="ui center aligned header">Cart</h1>
        <div className="ui divider" />
        <Page
          isLoading={!isReady && !error}
          contentError={error}
          content={
            isReady ?
              <Cart
                cart={cart}
                cartProducts={cartProducts}
                festivals={festivals}
                removeCartProduct={this.removeCartProduct}
                selectFestival={this.selectFestival}
                updateQuantity={this.updateQuantity}
                onCheckout={this.onCheckout}
              />
            : ''
          }
        />
      </div>
    )
  }
}
