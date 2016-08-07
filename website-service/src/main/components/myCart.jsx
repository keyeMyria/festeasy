import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Option } from 'semantic-react'
import moment from 'moment'
import PriceFormatter from 'utils/priceFormatter.jsx'
import MySelect from 'utils/mySelect.jsx'
import { MyTable, MyTr, MyTd, MyTh } from 'utils/table.jsx'
import MyOnBlurInput from 'utils/myOnBlurInput.jsx'
import MyButton from 'utils/myButton.jsx'


export default class Cart extends React.Component {
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
      cart,
      cartProducts,
      festivals,
      updateQuantity,
      onCheckout,
      removeCartProduct,
    } = this.props

    const options = festivals.map((festival) => (
      <Option key={festival.id} value={festival.id}>
        {festival.name} - {moment(festival.starts_on).format('YYYY')}
      </Option>
    ))

    const headers = (
      <MyTr>
        <MyTh>Product</MyTh>
        <MyTh>Quantity</MyTh>
        <MyTh>Sub Total</MyTh>
        <MyTh />
      </MyTr>
    )

    const rows = cartProducts.map((cp) => (
      <MyTr key={cp.id}>
        <MyTd>{cp.product.name}</MyTd>
        <MyTd>
          <MyOnBlurInput
            type="number"
            onBlur={(e) => updateQuantity(cp, e.target.value)}
            initialValue={cp.quantity}
          />
        </MyTd>
        <MyTd>
          <PriceFormatter rands={cp.sub_total_rands} />
        </MyTd>
        <MyTd>
          <MyButton onClick={() => removeCartProduct(cp)}>
            Remove
          </MyButton>
        </MyTd>
      </MyTr>
    ))
    return (
      <div className="ui segment">
        <label htmlFor="MySelect">Select festival:</label>
        <MySelect
          fluid
          placeholder="Select festival"
          selected={cart.festival_id ? [cart.festival_id] : []}
          updateSelected={(selected) => this.props.selectFestival(selected[0])}
          options={options}
        />
        {!cart.festival_id ?
          <div className="ui compact blue message">
            Please select a festival
          </div>
        : ''}
        <MyTable
          headers={headers}
          rows={rows}
        />
        <div>
          <div>Total: <PriceFormatter rands={cart.total_rands} /></div>
          <button
            className="ui positive button"
            onClick={onCheckout}
            disabled={!(cart.festival_id && cartProducts.length > 0)}
          >
            Secure Checkout
          </button>
        </div>
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
