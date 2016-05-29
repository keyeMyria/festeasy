import React, { PropTypes } from 'react'
import { Link } from 'react-router'


export default class Checkout extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
      cart: null,
      error: null,
    }
    this.getCart = this.getCart.bind(this)
  }

  getChildContext() {
    const { cart } = this.state
    return {
      cart,
    }
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
    let content = null
    if (cart) {
      content = this.props.children
    } else if (error) {
      content = <div>Error.</div>
    } else {
      content = <div>Loading...</div>
    }
    return (
      <div>
        <h1 className="ui header">Checkout</h1>
        <div className="ui ordered steps">
          <Link to="/cart" className="completed step">
            <div className="content">
              <div className="title">Cart</div>
              <div className="description">Choose your products and festival</div>
            </div>
          </Link>
          <Link to="/checkout/review" className="step" activeClassName="active">
            <div className="content">
              <div className="title">Review</div>
              <div className="description">Review your cart</div>
            </div>
          </Link>
          <Link to="/checkout/payment" className="step" activeClassName="active">
            <div className="content">
              <div className="title">Payment</div>
              <div className="description">Make payment</div>
            </div>
          </Link>
          <div className="step">
            <div className="content">
              <div className="title">Confirmation</div>
              <div className="description">Recieve payment confirmation</div>
            </div>
          </div>
        </div>
        {content}
      </div>
    )
  }
}

Checkout.propTypes = {
  children: PropTypes.any.isRequired,
}

Checkout.contextTypes = {
  store: PropTypes.object.isRequired,
  authUser: PropTypes.object.isRequired,
}

Checkout.childContextTypes = {
  cart: PropTypes.object,
}
