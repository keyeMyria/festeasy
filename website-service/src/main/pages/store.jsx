import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import AddToCartButton from 'main/addToCartButton.jsx'
import Page from 'common/page.jsx'


class ProductListItem extends React.Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
  }

  render() {
    const { product } = this.props
    return (
      <div>
        <Link to={`/products/${product.id}`}>
          <h3>{product.name}</h3>
        </Link>
        <p>{product.description}</p>
        <p>Price: {product.price_rands}</p>
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
    return (
      <div>
        <h1>Store</h1>
        {products.map(product => (
          <ProductListItem key={product.id} product={product} />
        ))}
      </div>
    )
  }
}


export default class ProductListContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      products: null,
    }
  }

  componentWillMount() {
    const { store } = this.context
    store.findAll('product')
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
