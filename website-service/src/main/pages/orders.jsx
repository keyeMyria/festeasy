import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import Page from 'utils/page.jsx'


class Orders extends React.Component {
  static propTypes = {
    orders: PropTypes.array.isRequired,
  }

  render() {
    const { orders } = this.props
    return (
      <div>
        <table className="ui table">
          <thead>
            <tr>
              <th>Order ID</th>
              <th>Festival</th>
              <th>Total</th>
              <th>Amount Due</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {orders.map((o) => (
              <tr key={o.id}>
                <td>Order {o.id}</td>
                <td>{o.festival.name}</td>
                <td>R{o.total_rands}</td>
                <td>R{o.current_invoice.amount_due_rands}</td>
                <td><Link to={`/account/orders/${o.id}/payment`}>Make payment</Link></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
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
