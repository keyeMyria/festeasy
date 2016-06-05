import React, { PropTypes } from 'react'
import Payment from '../../payment.jsx'


export default class PaymentContainer extends React.Component {
  render() {
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    return (
      <Payment invoiceId={invoiceId} />
    )
  }
}

PaymentContainer.propTypes = {
  location: PropTypes.object.isRequired,
}
