import React, { PropTypes } from 'react';

export default class CartItem extends React.Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }
  render() {
    const { cartProduct, updateQuantity, removeCartProduct } = this.props
    console.log('cartProduct: ', cartProduct)
    return (
      <div>
        <div className="ui items">
          <div className="item">
            <div className="ui tiny image">
              <img src="/images/beer.png" role="presentation" />
            </div>
            <div className="content">
              <a className="header">{cartProduct.product.name}</a>
              <div className="meta">
                <span>{cartProduct.product.description}</span>
              </div>
              <div className="description">
                <p>{parseInt(cartProduct.quantity, 10)}</p>
              </div>
              <div className="extra">
                Have a jolly good time in the sun
              </div>
            </div>
          </div>
        </div>
        <div className="ui divider" />
      </div>
    )
  }
}
