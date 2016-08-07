import React, { PropTypes } from 'react'
import Page from 'utils/page.jsx'
import Invoice from 'main/myInvoice.jsx'


export default class InvoiceContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    invoiceId: PropTypes.number.isRequired,
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
    const { invoiceId } = this.props
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
    const { invoiceId } = this.props
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
