import React, { PropTypes } from 'react'
import PriceFormatter from 'utils/priceFormatter.jsx'


export default class Invoice extends React.Component {
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
