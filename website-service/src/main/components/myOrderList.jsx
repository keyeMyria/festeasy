import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Table, Tr, Td } from 'semantic-react'


export default class OrderList extends React.Component {
  static propTypes = {
    orders: PropTypes.array.isRequired,
  }

  render() {
    const { orders } = this.props
    return (
      <Table>
        <thead>
          <Tr>
            <th>Order ID</th>
            <th>Festival</th>
            <th>Total</th>
            <th>Amount Due</th>
            <th />
          </Tr>
        </thead>
        <tbody>
          {orders.map((o) => (
            <Tr key={o.id}>
              <Td>{o.id}</Td>
              <Td>{o.festival.name}</Td>
              <Td>{o.total_rands}</Td>
              <Td>{o.current_invoice.amount_due_rands}</Td>
              <Td>
                <Link to={`/account/orders/${o.id}/invoice`}>See invoice</Link>
              </Td>
            </Tr>
          ))}
        </tbody>
      </Table>
    )
  }
}
