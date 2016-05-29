import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'


class Payment extends React.Component {
  render() {
    const { makePayment } = this.props
    return (
      <div>
        <h2 className="ui header">Payment</h2>
        <Button onClick={makePayment}>Make Payment</Button>
      </div>
    )
  }
}

Payment.propTypes = {
  makePayment: PropTypes.func.isRequired,
}


export default class PaymentContainer extends React.Component {
  constructor() {
    super()
    this.makePayment = this.makePayment.bind(this)
  }

  makePayment() {
    console.log('About to make payment.')
  }

  render() {
    return (
      <Payment
        makePayment={this.makePayment}
      />
    )
  }
}

PaymentContainer.contextTypes = {
  cart: PropTypes.object.isRequired,
}
