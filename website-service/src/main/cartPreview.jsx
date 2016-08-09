import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Option } from 'semantic-react'
import moment from 'moment'
import PriceFormatter from 'utils/priceFormatter.jsx'
import MySelect from 'utils/mySelect.jsx'
import CartRow from 'main/myCartRow.jsx'
import CartPanel from './cartPanel.jsx'


export default class CartPreview extends React.Component {
  static propTypes = {
    cart: PropTypes.object.isRequired,
    cartProducts: PropTypes.array.isRequired,
    festivals: PropTypes.array.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
    selectFestival: PropTypes.func.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    onCheckout: PropTypes.func.isRequired,
  }

  getMain() {
    const {
      cartProducts,
      updateQuantity,
      removeCartProduct,
    } = this.props
    return (
      <div>
        <CartPanel>
          {cartProducts.map((cartProduct) => (
            <CartRow
              updateQuantity={updateQuantity}
              removeCartProduct={removeCartProduct}
              key={cartProduct.id}
              cartProduct={cartProduct}
            />
          ))}
        </CartPanel>
      </div>
    )
  }

  render() {
    const { cartProducts } = this.props
    let result
    if (cartProducts.length === 0) {
      result = (
        <h2 className="ui center aligned header">
          Cart Empty
          <div className="sub header">
            <Link to="/store">Continue shopping</Link>
          </div>
        </h2>
      )
    } else {
      result = this.getMain()
    }
    return result
  }
}
