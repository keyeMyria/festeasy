import React, { PropTypes } from 'react'
import { Link } from 'react-router'


export default class Checkout extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
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
        {this.props.children}
      </div>
    )
  }
}
