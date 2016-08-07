import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { MyTable, MyTr, MyTd, MyTh } from 'utils/myTable.jsx'


export default class OrderList extends React.Component {
  static propTypes = {
    orders: PropTypes.array.isRequired,
  }

  render() {
    const { orders } = this.props
    return (
      <MyTable
        headers={
          <MyTr>
            <MyTh>Order ID</MyTh>
            <MyTh>Festival</MyTh>
            <MyTh>Total</MyTh>
            <MyTh>Amount Due</MyTh>
            <MyTh />
          </MyTr>
        }
        rows={
          orders.map((o) => (
            <MyTr key={o.id}>
              <MyTd>{o.id}</MyTd>
              <MyTd>{o.festival.name}</MyTd>
              <MyTd>{o.total_rands}</MyTd>
              <MyTd>{o.current_invoice.amount_due_rands}</MyTd>
              <MyTd>
                <Link to={`/account/orders/${o.id}/invoice`}>See invoice</Link>
              </MyTd>
            </MyTr>
          ))
        }
      />
    )
  }
}
