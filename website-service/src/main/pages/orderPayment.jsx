import React, { PropTypes } from 'react'
import Payment from '../payment.jsx'


export default class OrderPayment extends React.Component {
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
    const { order, error } = this.state
    let result
    if (order) {
      const invoiceId = order.current_invoice.id
      result = <Payment invoiceId={invoiceId} />
    } else if (error) {
      result = <div>Something went wrong.</div>
    } else {
      result = <div>Loading... probably</div>
    }
    return result
  }
}

OrderPayment.propTypes = {
  params: PropTypes.object.isRequired,
}

OrderPayment.contextTypes = {
  store: PropTypes.object.isRequired,
}
