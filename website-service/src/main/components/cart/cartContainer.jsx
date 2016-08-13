import React, { PropTypes } from 'react'
import Page from 'utils/page.jsx'


export default class CartContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    router: PropTypes.object.isRequired,
    authDetails: PropTypes.object.isRequired,
  }

  static propTypes = {
    children: PropTypes.any,
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
    this.renderChildren = this.renderChildren.bind(this)
  }

  componentDidMount() {
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
          error: 'Something went wrong in remove',
        })
      })
  }

  updateQuantity(cp) {
    const { store } = this.context
    store.update(
      'cartProduct',
      cp.id,
      { quantity: cp.quantity },
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
  renderChildren() {
    const { cart, cartProducts, festivals } = this.state
    const childrenWithProps = React.Children.map(this.props.children, (child) =>
      React.cloneElement(child, {
        cart: cart,
        cartProducts: cartProducts,
        festivals: festivals,
        removeCartProduct: this.removeCartProduct,
        selectFestival: this.selectFestival,
        updateQuantity: this.updateQuantity,
        onCheckout: this.onCheckout,
      }))
    return childrenWithProps
  }

  render() {
    const { cart, cartProducts, festivals, error } = this.state
    const isReady = cart && cartProducts && festivals
    return (
      <div>
        <Page
          isLoading={!isReady && !error}
          contentError={error}
          content={
            isReady ?
              <div>
                {this.renderChildren()}
              </div>
            : ''
          }
        />
      </div>
    )
  }
}
