import React, { PropTypes } from 'react'


class Review extends React.Component {
  render() {
    const { cart } = this.props
    const festival = cart.festival
    return (
      <div>
        <h1 className="ui header">Review Cart</h1>
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
      </div>
    )
  }
}

Review.propTypes = {
  cart: PropTypes.object.isRequired,
}


export default class ReviewContainer extends React.Component {
  constructor() {
    super()
    this.state = {
      loading: true,
      cart: null,
      error: null,
    }
    this.getCart = this.getCart.bind(this)
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
  }

  render() {
    const { cart, error } = this.state
    if (cart) {
      return (
        <div>
          <Review
            cart={cart}
          />
        </div>
      )
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading.</div>
    }
  }
}

ReviewContainer.contextTypes = {
  store: PropTypes.object.isRequired,
  authUser: PropTypes.object.isRequired,
}
