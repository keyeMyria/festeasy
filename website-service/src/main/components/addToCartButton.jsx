import React, { PropTypes } from 'react'
import { Button, Input } from 'semantic-react'


export default class AddToCartButton extends React.Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
  }

  static contextTypes = {
    store: PropTypes.object.isRequired,
    authDetails: PropTypes.object,
    addNotification: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
      quantity: 1,
    }
    this.onClick = this.onClick.bind(this)
    this.onChange = this.onChange.bind(this)
  }

  onClick() {
    const { store, authDetails, addNotification } = this.context
    if (authDetails) {
      store.find('user', authDetails.userId)
        .then((user) => {
          store.create('cartProduct', {
            'cart_id': user.cart_id,
            'product_id': this.props.product.id,
            quantity: this.state.quantity,
          })
            .then(() => {
              addNotification({
                message: 'Successfully added product to cart',
                level: 'success',
              })
            })
            .catch((error) => {
              let message = 'Something went wrong'
              let level = 'error'
              if (error.status === 409) {
                message = 'Item already in cart'
                level = 'warning'
              }
              addNotification({
                message,
                level,
              })
            })
        })
    }
    if (!authDetails) {
      addNotification({
        message: 'Please sign in',
        level: 'warning',
      })
    }
  }

  onChange(e) {
    this.setState({ quantity: e.target.value })
  }

  render() {
    return (
      <div>
        <Input
          required
          type="number"
          min={1}
          max={10}
          value={this.state.quantity}
          onChange={this.onChange}
        />
        <Button basic color="green" onClick={this.onClick}>Add to cart</Button>
      </div>
    )
  }
}
