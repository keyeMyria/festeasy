import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import {
  Grid,
  Column,
  Header,
  SubHeader,
  Label,
  Message,
  Button,
  Option,
  Table,
  Tr,
  Td,
} from 'semantic-react'
import moment from 'moment'
import PriceFormatter from 'utils/priceFormatter.jsx'
import MySelect from 'utils/mySelect.jsx'
import MyStatefulInput from 'utils/myStatefulInput.jsx'
import ProductImage from 'main/components/productImage.jsx'


export default class Cart extends React.Component {
  static propTypes = {
    cart: PropTypes.object,
    cartProducts: PropTypes.array,
    festivals: PropTypes.array,
    removeCartProduct: PropTypes.func,
    selectFestival: PropTypes.func,
    updateQuantity: PropTypes.func,
    onCheckout: PropTypes.func,
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
    return (
      <div className="ui segment">
        {!cart.festival_id ?
          <Message emphasis="warning">
            Please select a festival below
          </Message>
        : ''}
        <Label>Select festival:</Label>
        <MySelect
          fluid
          placeholder="Select festival..."
          selected={cart.festival_id ? [cart.festival_id] : []}
          updateSelected={(selected) => this.props.selectFestival(selected[0])}
          options={options}
        />
        <Table>
          <thead>
            <Tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sub Total</th>
              <th />
            </Tr>
          </thead>
          <tbody>
            {cartProducts.map((cp) => (
              <Tr key={cp.id}>
                <Td>
                  <Link to={`/store/products/${cp.product.id}`}>
                    <Grid columns={2}>
                      <Column width={3}>
                        <ProductImage product={cp.product} maxHeight={40} />
                      </Column>
                      <Column>
                        {cp.product.name}
                      </Column>
                    </Grid>
                  </Link>
                </Td>
                <Td>
                  <MyStatefulInput
                    type="number"
                    min={1}
                    max={10}
                    initialValue={cp.quantity}
                    onBlur={(e) => updateQuantity(cp, e.target.value)}
                  />
                </Td>
                <Td>
                  <PriceFormatter rands={cp.sub_total_rands} />
                </Td>
                <Td>
                  <Button onClick={() => removeCartProduct(cp)}>
                    Remove
                  </Button>
                </Td>
              </Tr>
            ))}
          </tbody>
        </Table>
        <div>
          <div>Total: <PriceFormatter rands={cart.total_rands} /></div>
          <Button
            onClick={onCheckout}
            disabled={!(cart.festival_id && cartProducts.length > 0)}
          >
            Secure Checkout
          </Button>
        </div>
      </div>
    )
  }

  render() {
    const { cartProducts } = this.props
    let result
    if (cartProducts.length === 0) {
      result = (
        <Header aligned="center">
          Cart Empty
          <SubHeader>
            <Link to="/store">Continue shopping</Link>
          </SubHeader>
        </Header>
      )
    } else {
      result = this.getMain()
    }
    return result
  }
}
