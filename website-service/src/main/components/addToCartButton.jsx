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
      isLoading: false,
    }
    this.onClick = this.onClick.bind(this)
    this.onChange = this.onChange.bind(this)
  }

  onClick() {
    const { store, authDetails, addNotification } = this.context
    if (authDetails) {
      this.setState({ isLoading: true })
      store.find('user', authDetails.userId)
        .then((user) => {
          store.create('cartProduct', {
            'cart_id': user.cart_id,
            'product_id': this.props.product.id,
            quantity: this.state.quantity,
          })
            .then(() => {
              this.setState({ isLoading: false })
              addNotification({
                message: 'Successfully added product to cart',
                level: 'success',
              })
            })
            .catch((error) => {
              this.setState({ isLoading: false })
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
    const { isLoading, quantity } = this.state
    return (
      <div>
        <Input
          disabled={isLoading}
          required
          type="number"
          min={1}
          max={10}
          value={quantity}
          onChange={this.onChange}
        />
        <Button
          state={isLoading ? 'loading' : ''}
          basic
          color="green"
          onClick={this.onClick}
        >
          Add to cart
        </Button>
      </div>
    )
  }
}
