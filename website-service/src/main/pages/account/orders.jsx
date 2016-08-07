import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import Page from 'utils/page.jsx'
import { MyTable, MyTr, MyTd, MyTh } from 'utils/myTable.jsx'


class Orders extends React.Component {
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


export default class OrdersContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      orders: null,
      error: null,
    }
    this.fetchOrders = this.fetchOrders.bind(this)
  }

  componentWillMount() {
    this.fetchOrders()
  }

  fetchOrders() {
    const { store } = this.context
    store.findAll('order')
      .then((orders) => {
        this.setState({
          orders,
          error: null,
        })
      })
      .catch((error) => {
        this.setState({
          error,
        })
      })
  }

  render() {
    const { orders, error } = this.state
    return (
      <Page
        header={<h2 className="ui header">Orders</h2>}
        isLoading={!orders && !error}
        contentError={error}
        content={
          orders ? <Orders orders={orders} /> : ''
        }
      />
    )
  }
}
