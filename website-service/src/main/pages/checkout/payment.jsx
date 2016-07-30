import React, { PropTypes } from 'react'
import Payment from 'main/payment.jsx'


export default class PaymentContainer extends React.Component {
  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  render() {
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    return (
      <Payment invoiceId={invoiceId} />
    )
  }
}
