import React, { PropTypes } from 'react'
import InvoiceContainer from 'main/components/myInvoiceContainer.jsx'


export default class Invoice extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      invoice: null,
      error: null,
    }
  }

  componentDidMount() {
    this.fetchInvoice()
  }

  fetchInvoice() {
    const { store } = this.context
    const { orderId } = this.props.params
    store.find('order', orderId)
      .then((order) => {
        this.setState({
          invoice: order.current_invoice,
          error: null,
        })
      })
  }

  render() {
    const { invoice, error } = this.state
    let result
    if (error) {
      result = <div>Something went wrong</div>
    } else if (invoice) {
      result = <InvoiceContainer invoiceId={invoice.id} />
    } else {
      result = <div>Something unexpected happened</div>
    }
    return result
  }
}
