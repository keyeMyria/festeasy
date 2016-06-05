import React, { PropTypes } from 'react'


export default class AddToCartButton extends React.Component {
  constructor(props) {
    super(props)
    this.onClick = this.onClick.bind(this)
  }

  onClick() {
    const { store, authSession } = this.context
    if (authSession) {
      store.find('user', authSession.user_id)
      .then((user) => {
        store.create('cartProduct', {
          'cart_id': user.cart_id,
          'product_id': this.props.product.id,
        })
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
}
