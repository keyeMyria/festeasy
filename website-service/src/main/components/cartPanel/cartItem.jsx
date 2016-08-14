import React, { PropTypes } from 'react';
import apiEndpoint from 'apiEndpoint.js'
import { Image, Button } from 'semantic-react'
import MyStatefulInput from 'utils/myStatefulInput.jsx'

export default class CartItem extends React.Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }
  render() {
    // , updateQuantity, removeCartProduct
    const { cartProduct, updateQuantity, removeCartProduct } = this.props
    return (
      <div className="ui grid">
        <div className="three wide column">
          {cartProduct.product.thumbnail_image_id ?
            <Image
              centered
              style={{ 'maxHeight': '270px', width: '60px', height: '60px' }}
              alt="product thumbnail"
              src={apiEndpoint.concat(`v1/images/${cartProduct.product.thumbnail_image_id}/image`)}
            /> : 'No thumbnail image'
          }
        </div>
        <div className="nine wide column">
          <div className="row ui header">
          {cartProduct.product.name}
          </div>
          <div className="row">
          {cartProduct.product.description}
          </div>
        </div>
        <div className="four wide column">
          <MyStatefulInput
            type="number"
            min={1}
            max={10}
            initialValue={cartProduct.quantity}
            onBlur={(e) => updateQuantity(cartProduct, e.target.value)}
          />
          <div>
            R {cartProduct.sub_total_rands}
          </div>
          <a onClick={() => removeCartProduct(cartProduct)}>
            Remove
          </a>
        </div>

      </div>
    )
  } }
