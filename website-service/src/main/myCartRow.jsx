import React, { PropTypes } from 'react'
import { Input } from 'semantic-react'
import update from 'react-addons-update'
import PriceFormatter from 'utils/priceFormatter.jsx'


export default class CartRow extends React.Component {
  static propTypes = {
    cartProduct: PropTypes.object.isRequired,
    updateQuantity: PropTypes.func.isRequired,
    removeCartProduct: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      cartProduct: props.cartProduct,
    }
    this.onBlur = this.onBlur.bind(this)
  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      cartProduct: nextProps.cartProduct,
    })
  }

  onBlur() {
    this.props.updateQuantity(this.state.cartProduct)
  }

  updateQuantity(e) {
    const { cartProduct } = this.state
    this.setState({
      cartProduct: update(cartProduct, { $merge: { quantity: e.target.value } }),
    })
  }

  render() {
    const { cartProduct } = this.state
    return (
      <tr>
        <td>{cartProduct.product.name}</td>
        <td>
          <Input
            type="number"
            onChange={(e) => this.updateQuantity(e)}
            onBlur={this.onBlur}
            value={cartProduct.quantity}
            min={1}
            max={10}
          />
        </td>
        <td><PriceFormatter rands={cartProduct.sub_total_rands} /></td>
        <td>
          <button
            className="ui orange button"
            onClick={() => { this.props.removeCartProduct(cartProduct) }}
          >
            Remove from cart
          </button>
        </td>
      </tr>
    )
  }
}
