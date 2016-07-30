import React, { PropTypes } from 'react'


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
    this.onClick = this.onClick.bind(this)
  }

  onClick() {
    const { store, authDetails, addNotification } = this.context
    if (authDetails) {
      store.find('user', authDetails.userId)
        .then((user) => {
          store.create('cartProduct', {
            'cart_id': user.cart_id,
            'product_id': this.props.product.id,
          })
            .then(() => {
              addNotification({
                message: 'Successfully added product to cart.',
                level: 'success',
              })
            })
            .catch(() => {
              addNotification({
                message: 'Something went wrong',
                level: 'warning',
              })
            })
        })
    }
    if (!authDetails) {
      addNotification({
        message: 'Please sign in to add products.',
        level: 'warning',
      })
    }
  }

  render() {
    return (
      <button className="ui button" onClick={this.onClick}>Add to cart</button>
    )
  }
}
