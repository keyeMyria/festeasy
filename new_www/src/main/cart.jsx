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
            </tr>
          </thead>
          <tbody>
            {cart.cart_products.map((cartProduct) => (
              <tr key={cartProduct.id}>
                <td>{cartProduct.product.name}</td>
                <td>{cartProduct.quantity}</td>
                <td>{cartProduct.sub_total_rands}</td>
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
}


export default class CartContainer extends React.Component {
  constructor(props, context) {
    super(props)
    this.state = {
      loading: true,
      cart: null,
      error: null,
    }
    if (context.authUser) {
      context.store.find('cart', context.authUser.cart_id)
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
  }

  render() {
    const { cart, error } = this.state
    if (cart) {
      return <Cart cart={cart} />
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
