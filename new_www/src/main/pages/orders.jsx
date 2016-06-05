import React, { PropTypes } from 'react'
import { Link } from 'react-router'


class Orders extends React.Component {
  render() {
    const { orders } = this.props
    return (
      <div>
        <table className="ui table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Festival</th>
              <th>Total</th>
              <th>Amount Due</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {orders.map((o) => (
              <tr key={o.id}>
                <td><Link to={`/account/orders/${o.id}`}>{o.id}</Link></td>
                <td>{o.festival.name}</td>
                <td>R{o.total_rands}</td>
                <td>R{o.current_invoice.amount_due_rands}</td>
                <td><button className="ui button">Make Payment</button></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )
  }
}

Orders.propTypes = {
  orders: PropTypes.array.isRequired,
}


export default class OrdersContainer extends React.Component {
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
    let result
    if (orders) {
      result = <Orders orders={orders} />
    } else if (error) {
      result = <div>Something went wrong.</div>
    } else {
      result = <div>Loading... probably</div>
    }
    return (
      <div>
        <h1 className="ui header">Orders</h1>
        {result}
      </div>
    )
  }
}

OrdersContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}
