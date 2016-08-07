import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import AddToCartButton from 'main/components/addToCartButton.jsx'
import Page from 'utils/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


class ProductListItem extends React.Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
  }

  render() {
    const { product } = this.props
    return (
      <div>
        <Link to={`/store/products/${product.id}`}>
          <h3>{product.name}</h3>
        </Link>
        <p>{product.description}</p>
        <p>Price: <PriceFormatter rands={product.price_rands} /></p>
        <AddToCartButton product={product} />
      </div>
    )
  }
}


class ProductList extends React.Component {
  static propTypes = {
    products: PropTypes.arrayOf(
      PropTypes.object
    ).isRequired,
  }

  render() {
    const { products } = this.props
    let result
    if (products.length === 0) {
      result = <div>No results</div>
    } else {
      result = (
        products.map(product => (
          <div key={product.id}>
            <ProductListItem product={product} />
            <div className="ui divider" />
          </div>
        ))
      )
    }
    return <div>{result}</div>
  }
}


export default class ProductListContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      products: null,
    }
    this.fetchProducts = this.fetchProducts.bind(this)
  }

  componentDidMount() {
    this.fetchProducts({})
  }

  componentWillReceiveProps(nextProps) {
    this.fetchProducts({
      search: nextProps.location.query.search,
    })
  }

  fetchProducts(params) {
    const { store } = this.context
    const config = { bypassCache: true }
    store.findAll('product', params, config)
      .then((products) => {
        this.setState({
          loading: false,
          error: null,
          products,
        })
      })
      .catch(() => {
        this.setState({
          loading: false,
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { products, error } = this.state
    return (
      <Page
        isLoading={!products && !error}
        contentError={error}
        content={
          products ? <ProductList products={products} /> : ''
        }
      />
    )
  }
}
