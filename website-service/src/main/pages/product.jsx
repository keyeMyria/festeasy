import React, { PropTypes } from 'react';
import Page from 'common/page.jsx'
import AddToCartButton from 'main/addToCartButton.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


class Product extends React.Component {
  render() {
    const { product } = this.props
    return (
      <div>
        <h2 className="ui center aligned header">{product.name}</h2>
        <p>{product.description}</p>
        <p>Price: <PriceFormatter rands={product.price_rands} /></p>
        <AddToCartButton product={product} />
      </div>
    )
  }
}

Product.propTypes = {
  product: PropTypes.object.isRequired,
}


export default class ProductContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      product: null,
    }
  }

  componentWillMount() {
    const { store } = this.context
    store.find('product', this.props.params.productId, { bypassCache: true })
      .then((product) => {
        this.setState({
          product,
          error: null,
        })
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { product, error } = this.state
    return (
      <Page
        isLoading={!product && !error}
        contentError={error}
        content={
          product ? <Product product={product} /> : ''
        }
      />
    )
  }
}
