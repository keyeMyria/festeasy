import React, { PropTypes, Component } from 'react'
import MyStatefulInput from 'utils/myStatefulInput.jsx'
import ProductImage from 'main/components/productImage.jsx'


export default class CartItem extends Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }

  render() {
    // , updateQuantity, removeCartProduct
    const { cartProduct, updateQuantity, removeCartProduct } = this.props
    return (
      <div className="ui grid" >
        <div className="three wide column">
          <ProductImage product={cartProduct.product} />
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
  }
}
