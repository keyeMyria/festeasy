import React, { PropTypes } from 'react'
import InvoiceContainer from 'main/myInvoiceContainer.jsx'


export default class Payment extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  render() {
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    return (
      <InvoiceContainer invoiceId={invoiceId} />
    )
  }
}
