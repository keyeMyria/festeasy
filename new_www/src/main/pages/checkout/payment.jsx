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
    const queryParams = this.props.location.query
    this.context.store.create('payu-transaction', {
      invoice_id: queryParams['invoice-id'],
    })
    .then((response) => {
      const payUReference = response.payu_reference
      window.location.href = `https://staging.payu.co.za/rpp.do?PayUReference=${payUReference}`
    })
  }

  render() {
    return (
      <Payment
        makePayment={this.makePayment}
      />
    )
  }
}

PaymentContainer.propTypes = {
  location: PropTypes.object.isRequired,
}

PaymentContainer.contextTypes = {
  router: PropTypes.object.isRequired,
  store: PropTypes.object.isRequired,
}
