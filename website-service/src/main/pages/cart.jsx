import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Input, Option } from 'semantic-react'
import update from 'react-addons-update'
import PriceFormatter from 'utils/priceFormatter.jsx'
import MySelect from 'utils/mySelect.jsx'
import Page from 'common/page.jsx'


class CartRow extends React.Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      cartProduct: props.cartProduct,
    }
    this.onBlur = this.onBlur.bind(this)
  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      cartProduct: nextProps.cartProduct,
    })
  }

  onBlur() {
    this.props.updateQuantity(this.state.cartProduct)
  }

  updateQuantity(e) {
    const { cartProduct } = this.state
    this.setState({
      cartProduct: update(cartProduct, { $merge: { quantity: e.target.value } }),
    })
  }

  render() {
    const { cartProduct } = this.state
    return (
      <tr>
        <td>{cartProduct.product.name}</td>
        <td>
          <Input
            type="number"
            onChange={(e) => this.updateQuantity(e)}
            onBlur={this.onBlur}
            value={cartProduct.quantity}
            min={1}
            max={10}
          />
        </td>
        <td><PriceFormatter rands={cartProduct.sub_total_rands} /></td>
        <td>
          <button
            className="ui button"
            onClick={() => { this.props.removeCartProduct(cartProduct) }}
          >
            Remove
          </button>
        </td>
      </tr>
    )
  }
}


class Cart extends React.Component {
  static propTypes = {
    cart: PropTypes.object.isRequired,
    festivals: PropTypes.array.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
    selectFestival: PropTypes.func.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    onCheckout: PropTypes.func.isRequired,
  }

  getMain() {
    const {
      cart,
      festivals,
      updateQuantity,
      onCheckout,
      removeCartProduct,
    } = this.props
    const options = festivals.map((festival) => (
      <Option key={festival.id} value={festival.id}>{festival.name}</Option>
    ))
    return (
      <div className="ui segment">
        <label>Select festival:</label>
        <MySelect
          fluid
          placeholder="Select festival"
          selected={cart.festival_id ? [cart.festival_id] : []}
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
              <CartRow
                updateQuantity={updateQuantity}
                removeCartProduct={removeCartProduct}
                key={cartProduct.id}
                cartProduct={cartProduct}
              />
            ))}
          </tbody>
        </table>
        <div>
          <div>Total: <PriceFormatter rands={cart.total_rands} /></div>
          <div className="ui positive button" onClick={onCheckout}>Secure Checkout</div>
        </div>
      </div>
    )
  }

  render() {
    const { cart } = this.props
    let result
    if (cart.cart_products.length === 0) {
      result = (
        <h2 className="ui center aligned header">
          Cart Empty
          <div className="sub header">
            <Link to="/store">Continue shopping</Link>
          </div>
        </h2>
      )
    } else {
      result = this.getMain()
    }
    return result
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
    this.fetchCart = this.fetchCart.bind(this)
    this.removeCartProduct = this.removeCartProduct.bind(this)
    this.selectFestival = this.selectFestival.bind(this)
    this.updateQuantity = this.updateQuantity.bind(this)
  }

  componentDidMount() {
    this.fetchCart()
    this.fetchFestivals()
  }

  onCheckout() {
    this.context.router.push('/checkout/review')
  }

  fetchFestivals() {
    const { store } = this.context
    return new Promise((resolve, reject) => {
      store.findAll('festival')
        .then((festivals) => {
          this.setState({
            festivals,
          }, resolve(festivals))
        })
        .catch((error) => {
          this.setState({
            error: 'Something went wront',
          }, reject(error))
        })
    })
  }

  fetchCart() {
    return new Promise((resolve, reject) => {
      const { store, authDetails } = this.context
      store.find('user', authDetails.userId)
        .then((user) => {
          store.find('cart', user.id, { bypassCache: true })
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
  }

  selectFestival(festivalId) {
    return new Promise((resolve, reject) => {
      this.context.store.update(
        'cart',
        this.state.cart.id,
        { festival_id: festivalId },
        { method: 'PATCH' }
      )
        .then(() => {
          this.fetchCart()
            .then(() => {
              resolve()
            })
            .catch(() => {
              reject()
            })
        })
        .catch(() => {
          reject()
        })
    })
  }

  render() {
    const { cart, error, festivals } = this.state
    return (
      <div>
        <h1 className="ui center aligned header">Cart</h1>
        <div className="ui divider" />
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
              />
            : ''
          }
        />
      </div>
    )
  }
}
