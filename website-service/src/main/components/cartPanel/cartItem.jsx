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
    console.log('cartProduct: ', cartProduct)
    return (
      <div>
        <div className="ui items">
          <div className="item" style={{padding: '5px', border: '1px solid',  borderColor: '#6AA0D5', borderRadius: 20}}>
            <div style={{padding: '5px'}}>
              <p>{parseInt(cartProduct.quantity, 10)}X</p>
            </div>
            <a className="header">{cartProduct.product.name}</a>
            <div className="ui tiny image">
              {cartProduct.product.thumbnail_image_id ?
                <Image
                  centered
                  style={{ 'maxHeight': '270px', width: '70px', height: '70px' }}
                  alt="product thumbnail"
                  src={apiEndpoint.concat(`v1/images/${cartProduct.product.thumbnail_image_id}/image`)}
                /> : 'No thumbnail image'
              }
            </div>
            <div className="content">
              <div className="ui grid" >
                <div className="four wide column" >
                  <div className="meta">
                    <span>{cartProduct.product.description}</span>
                  </div>
                </div>
                <div className="four wide column" >
                  <div className="description">
                  </div>
                </div>
                <div className="four wide column" >
                  <div className="extra">
                    Have a jolly good time
                  </div>
                </div>
                <div className="four wide column" >
                  Total:
                  <div></div>
                  <div className="ui blue header">
                    {cartProduct.sub_total_rands}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="ui hidden divider" />
        </div>
      </div>
    )
  }
}
