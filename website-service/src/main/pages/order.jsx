import React, { PropTypes } from 'react'


class Order extends React.Component {
  render() {
    const { order } = this.props
    return (
      <div>
        <h1 className="ui header">Order {order.id}</h1>
        <table className="ui definition table">
          <tbody>
            <tr>
              <td className="three wide column">ID</td>
              <td>{order.id}</td>
            </tr>
            <tr>
              <td className="three wide column">Festival</td>
              <td>{order.festival.name}</td>
            </tr>
            <tr>
              <td className="three wide column">Total</td>
              <td>{order.total_rands}</td>
            </tr>
            <tr>
              <td className="three wide column">Amount Due</td>
              <td>{order.current_invoice.amount_due_rands}</td>
            </tr>
          </tbody>
        </table>
      </div>
    )
  }
}

Order.propTypes = {
  order: PropTypes.object.isRequired,
}


export default class OrderContainer extends React.Component {
  constructor() {
    super()
    this.state = {
      order: null,
      error: null,
    }
  }

  componentWillMount() {
    const { store } = this.context
    const { orderId } = this.props.params
    store.find('order', orderId)
      .then((order) => {
        this.setState({
          order,
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
    let result
    const { order, error } = this.state
    if (order) {
      result = <Order order={order} />
    } else if (error) {
      result = <div>Something went wrong.</div>
    } else {
      result = <div>Loading... probably.</div>
    }
    return (
      <div>
        {result}
      </div>
    )
  }
}

OrderContainer.propTypes = {
  params: PropTypes.object.isRequired,
}

OrderContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}
