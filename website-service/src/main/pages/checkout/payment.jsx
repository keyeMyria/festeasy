import React, { PropTypes } from 'react'
import Page from 'common/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


class Invoice extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    invoice: PropTypes.object.isRequired,
    invoiceProducts: PropTypes.object.isRequired,
  }

  render() {
    const { invoice, invoiceProducts } = this.props
    return (
      <div className="ui segment">
        <h2 className="ui center aligned header">Invoice {invoice.id}</h2>
        <table className="ui table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sub Total</th>
            </tr>
          </thead>
          <tbody>
            {invoiceProducts.map((ip) => (
              <tr key={ip.id}>
                <th>{ip.product.name}</th>
              </tr>
            ))}
          </tbody>
        </table>
        <div>
          Total: <PriceFormatter rands={invoice.total_rands} />
        </div>
      </div>
    )
  }
}


export default class InvoiceContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      invoice: null,
      error: null,
    }
    this.makePayment = this.makePayment.bind(this)
    this.fetchInvoice = this.fetchInvoice.bind(this)
  }

  componentDidMount() {
    this.fetchInvoice()
  }

  makePayment() {
    const { invoice } = this.state
    const { store } = this.context
    store.create('payu-transaction', {
      invoice_id: invoice.id,
    })
      .then((response) => {
        const payUReference = response.payu_reference
        window.location.href = `https://staging.payu.co.za/rpp.do?PayUReference=${payUReference}`
      })
  }

  fetchInvoice() {
    const { store } = this.context
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    store.find('invoice', invoiceId)
      .then((invoice) => {
        this.setState({ invoice })
      })
  }

  render() {
    const { invoice, error } = this.state
    const isReady = !!invoice
    return (
      <Page
        isLoading={!isReady && !error}
        contentError={error}
        content={
          isReady ?
            <Invoice invoice={invoice} />
          : ''
        }
      />
    )
  }
}
