import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'


export default class PaymentContainer extends React.Component {
  render() {
    return (
      <div>
        <h2 className="ui header">Payment</h2>
        <Button>Make Payment</Button>
      </div>
    )
  }
}

PaymentContainer.contextTypes = {
  cart: PropTypes.object.isRequired,
}
