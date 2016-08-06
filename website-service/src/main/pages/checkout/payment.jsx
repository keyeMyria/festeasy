import React, { PropTypes } from 'react'
import Page from 'common/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


class Invoice extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    invoice: PropTypes.object.isRequired,
    invoiceProducts: PropTypes.array.isRequired,
    makePayment: PropTypes.func,
  }

  render() {
    const { invoice, invoiceProducts, makePayment } = this.props
    return (
      <div className="ui segment">
        <h2 className="ui center aligned header">Invoice {invoice.id}</h2>
        <table className="ui table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Unit Price</th>
              <th>Sub Total</th>
            </tr>
          </thead>
          <tbody>
            {invoiceProducts.map((ip) => (
              <tr key={ip.id}>
                <td>{ip.product.name}</td>
                <td>{ip.quantity}</td>
                <td><PriceFormatter rands={ip.unit_price_rands} /></td>
                <td><PriceFormatter rands={ip.sub_total_rands} /></td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>
          Total due: <PriceFormatter rands={invoice.amount_due_rands} />
          <br />
          <button className="ui green button" onClick={makePayment}>Make payment</button>
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
      invoiceProducts: null,
      error: null,
    }
    this.makePayment = this.makePayment.bind(this)
    this.fetchInvoice = this.fetchInvoice.bind(this)
    this.fetchInvoiceProducts = this.fetchInvoiceProducts.bind(this)
  }

  componentDidMount() {
    this.fetchInvoice()
    this.fetchInvoiceProducts()
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
      .catch(() => {
        this.setState({
          error: 'Something went wrong making payment',
        })
      })
  }

  fetchInvoiceProducts() {
    const { store } = this.context
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    store.findAll('invoiceProduct', { 'invoice-id': invoiceId })
      .then((invoiceProducts) => {
        this.setState({ invoiceProducts })
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong fetching invoice line items',
        })
      })
  }

  fetchInvoice() {
    const { store } = this.context
    const invoiceId = parseInt(this.props.location.query['invoice-id'], 10)
    store.find('invoice', invoiceId)
      .then((invoice) => {
        this.setState({ invoice })
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong fetching invoice',
        })
      })
  }

  render() {
    const { invoice, invoiceProducts, error } = this.state
    const isReady = invoice && invoiceProducts
    return (
      <Page
        isLoading={!isReady && !error}
        contentError={error}
        content={
          isReady ?
            <Invoice
              invoice={invoice}
              invoiceProducts={invoiceProducts}
              makePayment={this.makePayment}
            />
          : ''
        }
      />
    )
  }
}
