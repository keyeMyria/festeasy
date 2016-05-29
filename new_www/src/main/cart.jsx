import React, { PropTypes } from 'react'
import { Select, Option } from 'semantic-react'


class MySelect extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      active: false,
      searchString: '',
    }
  }

  render() {
    const { fluid, options, placeholder, selected } = this.props
    const { active, searchString } = this.state
    return (
      <Select
        search
        selection
        fluid={fluid}
        active={active}
        selected={selected}
        placeholder={placeholder}
        onClick={() => this.setState({ active: true })}
        onRequestClose={() => this.setState({ active: false })}
        onSearchStringChange={string => this.setState({ searchString: string })}
        searchString={searchString}
        onSelectChange={val => this.props.updateSelected(val)}
      >
        {options.map((option) => (
          option
        ))}
      </Select>
    )
  }
}

MySelect.propTypes = {
  options: PropTypes.array.isRequired,
  updateSelected: PropTypes.func.isRequired,
  placeholder: PropTypes.string,
  selected: PropTypes.array,
  fluid: PropTypes.bool,
}


class Cart extends React.Component {
  render() {
    const { cart, festivals } = this.props
    const options = festivals.map((festival) => (
      <Option key={festival.id} value={festival.id}>{festival.name}</Option>
    ))
    return (
      <div>
        <MySelect
          fluid
          selected={[cart.festival_id]}
          updateSelected={(selected) => this.props.selectFestival(selected[0])}
          options={options}
        />
        <table className="ui table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sub Total</th>
              <th>Remove</th>
            </tr>
          </thead>
          <tbody>
            {cart.cart_products.map((cartProduct) => (
              <tr key={cartProduct.id}>
                <td>{cartProduct.product.name}</td>
                <td>{cartProduct.quantity}</td>
                <td>{cartProduct.sub_total_rands}</td>
                <td>
                  <button onClick={() => { this.props.removeCartProduct(cartProduct) }}>
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>Total: R{cart.total_rands}</div>
      </div>
    )
  }
}

Cart.propTypes = {
  cart: PropTypes.object.isRequired,
  festivals: PropTypes.array.isRequired,
  removeCartProduct: PropTypes.func.isRequired,
  selectFestival: PropTypes.func.isRequired,
}


export default class CartContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
      cart: null,
      festivals: null,
      error: null,
    }
    this.getCart = this.getCart.bind(this)
    this.removeCartProduct = this.removeCartProduct.bind(this)
    this.selectFestival = this.selectFestival.bind(this)
  }

  componentDidMount() {
    this.getCart()
  }

  getCart() {
    this.setState({ loading: true })
    const cart = this.context.store.find(
      'cart',
      this.context.authUser.cart_id,
      {
        bypassCache: true,
      }
    )
    const festivals = this.context.store.findAll('festival')
    Promise.all([cart, festivals])
    .then((values) => {
      this.setState({
        loading: false,
        cart: values[0],
        festivals: values[1],
      })
    })
    .catch(() => {
      this.setState({
        loading: false,
        error: 'Something went wrong.',
      })
    })
  }

  removeCartProduct(cp) {
    this.context.store.destroy('cartProduct', cp.id)
    .then(() => {
      this.getCart()
    })
  }

  selectFestival(festivalId) {
    this.context.store.update(
      'cart',
      this.state.cart.id,
      { festival_id: festivalId },
      { method: 'PATCH' }
    )
    .then(() => {
      this.getCart()
    })
  }

  render() {
    const { cart, error, festivals } = this.state
    if (cart && festivals) {
      return (
        <Cart
          cart={cart}
          festivals={festivals}
          removeCartProduct={this.removeCartProduct}
          selectFestival={this.selectFestival}
        />
      )
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading.</div>
    }
  }
}

CartContainer.contextTypes = {
  store: PropTypes.object.isRequired,
  authUser: PropTypes.object.isRequired,
}
