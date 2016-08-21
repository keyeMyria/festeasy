import React, { PropTypes } from 'react'
import { Header, Table, Tr, Td, Button } from 'semantic-react'
import PriceFormatter from 'utils/priceFormatter.jsx'


export default class Invoice extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    invoice: PropTypes.object.isRequired,
    invoiceProducts: PropTypes.array.isRequired,
    isCheckingOut: PropTypes.bool.isRequired,
    makePayment: PropTypes.func,
  }

  render() {
    const { invoice, invoiceProducts, makePayment, isCheckingOut } = this.props
    return (
      <div>
        <Header>Invoice {invoice.id}</Header>
        <Table>
          <thead>
            <Tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Unit Price</th>
              <th>Sub Total</th>
            </Tr>
          </thead>
          <tbody>
            {invoiceProducts.map((ip) => (
              <Tr key={ip.id}>
                <Td>{ip.product.name}</Td>
                <Td>{ip.quantity}</Td>
                <Td><PriceFormatter rands={ip.unit_price_rands} /></Td>
                <Td><PriceFormatter rands={ip.sub_total_rands} /></Td>
              </Tr>
            ))}
          </tbody>
        </Table>
        <div>
          Total due: <PriceFormatter rands={invoice.amount_due_rands} />
          <br />
          <Button onClick={makePayment} state={isCheckingOut ? 'loading' : ''}>Make payment</Button>
        </div>
      </div>
    )
  }
}
