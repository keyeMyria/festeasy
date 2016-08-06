import React, { PropTypes } from 'react'


export default class Checkout extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
    location: PropTypes.object.isRequired,
  }

  render() {
    const { pathname } = this.props.location
    return (
      <div>
        <h1 className="ui center aligned header">Checkout</h1>
        <div className="ui ordered steps">
          <div className="completed step">
            <div className="content">
              <div className="title">Cart</div>
              <div className="description">Choose your products and festival</div>
            </div>
          </div>
          <div className={'step '.concat(pathname === '/checkout/review' ? 'active' : '')}>
            <div className="content">
              <div className="title">Review</div>
              <div className="description">Review your cart</div>
            </div>
          </div>
          <div className={'step '.concat(pathname === '/checkout/payment' ? 'active' : '')}>
            <div className="content">
              <div className="title">Payment</div>
              <div className="description">Make payment</div>
            </div>
          </div>
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
