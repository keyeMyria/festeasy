import React, { PropTypes } from 'react'
import Payment from 'main/payment.jsx'
import Page from 'utils/page.jsx'


export default class OrderPayment extends React.Component {
  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

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
    return (
      <Page
        isLoading={!order && !error}
        content={
          order ? <Payment invoiceId={order.current_invoice.id} /> : ''
        }
      />
    )
  }
}
