import React, { PropTypes } from 'react';
import apiEndpoint from 'apiEndpoint.js'
import { Image } from 'semantic-react'

export default class CartItem extends React.Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }
  render() {
    // , updateQuantity, removeCartProduct
    const { cartProduct } = this.props
    return (
      <div>
        <div className="ui items">
          <div className="item">
            <div className="ui tiny image">
              {cartProduct.product.thumbnail_image_id ?
                <Image
                  centered
                  style={{ 'maxHeight': '270px', width: '90px', height: '90px' }}
                  alt="product thumbnail"
                  src={apiEndpoint.concat(`v1/images/${cartProduct.product.thumbnail_image_id}/image`)}
                /> : 'No thumbnail image'
              }
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
