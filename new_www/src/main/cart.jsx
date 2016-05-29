import React, { PropTypes } from 'react'


class Cart extends React.Component {
  render() {
    const { cart } = this.props
    return (
      <div>
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
                <td>{cartProduct.quantity}</td>
                <td>{cartProduct.sub_total_rands}</td>
                <td>
                  <button onClick={() => { this.props.removeCartProduct(cartProduct) }}>
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>Total: R{cart.total_rands}</div>
      </div>
    )
  }
}

Cart.propTypes = {
  cart: PropTypes.object.isRequired,
  removeCartProduct: PropTypes.func.isRequired,
}


export default class CartContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
      cart: null,
      festivals: [],
      error: null,
    }
    this.getCart = this.getCart.bind(this)
    this.removeCartProduct = this.removeCartProduct.bind(this)
  }

  componentDidMount() {
    this.getCart()
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
        cart: cart,
      })
    })
    .catch(() => {
      this.setState({
        loading: false,
        error: 'Something went wrong.',
      })
    })
  }

  removeCartProduct(cp) {
    this.context.store.destroy('cartProduct', cp.id)
    .then(() => {
      this.getCart()
    })
  }

  render() {
    const { cart, error, festivals } = this.state
    if (cart) {
      return (
        <Cart
          cart={cart}
          festivals={festivals}
          removeCartProduct={this.removeCartProduct}
        />
      )
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading.</div>
    }
  }
}

CartContainer.contextTypes = {
  store: PropTypes.object.isRequired,
  authUser: PropTypes.object.isRequired,
}
