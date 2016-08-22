import React, { PropTypes } from 'react'
import { Header } from 'semantic-react'
import Page from 'utils/page.jsx'
import OrderList from 'main/components/myOrderList.jsx'


export default class OrderListContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    authDetails: PropTypes.object,
  }

  constructor() {
    super()
    this.state = {
      orders: null,
      error: null,
    }
    this.fetchOrders = this.fetchOrders.bind(this)
  }

  componentDidMount() {
    this.fetchOrders()
  }

  fetchOrders() {
    const { store, authDetails } = this.context
    store.findAll('order', { 'user-id': authDetails.userId }, { bypassCache: true })
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
        header={<Header>Orders</Header>}
        isLoading={!orders && !error}
        contentError={error}
        content={
          orders ? <OrderList orders={orders} /> : ''
        }
      />
    )
  }
}
