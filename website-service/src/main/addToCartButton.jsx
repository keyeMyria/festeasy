import React, { PropTypes } from 'react'


export default class AddToCartButton extends React.Component {
  constructor(props) {
    super(props)
    this.onClick = this.onClick.bind(this)
  }

  onClick() {
    const { store, authSession, addNotification } = this.context
    if (authSession) {
      store.find('user', authSession.user_id)
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
            .catch((error) => {
              if (error.status === 409) {
                addNotification({
                  message: 'Product already in cart.',
                  level: 'warning',
                })
              }
            })
        })
    } else {
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

AddToCartButton.propTypes = {
  product: PropTypes.object.isRequired,
}

AddToCartButton.contextTypes = {
  store: PropTypes.object.isRequired,
  authSession: PropTypes.object,
  addNotification: PropTypes.func.isRequired,
}
