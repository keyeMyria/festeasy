import React, { PropTypes } from 'react';
import { Link } from 'react-router';


class ProductListItem extends React.Component {
  render() {
    const { product } = this.props
    return (
      <div>
        <Link to={`/products/${product.id}`}>
          <h3>{product.name}</h3>
        </Link>
        <p>{product.description}</p>
        <p>Price: {product.price_rands}</p>
      </div>
    )
  }
}

ProductListItem.propTypes = {
  product: PropTypes.object.isRequired,
}


class ProductList extends React.Component {
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

ProductList.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.object
  ).isRequired,
}


export default class ProductListContainer extends React.Component {
  constructor(props, context) {
    super(props)
    this.state = {
      loading: true,
      error: null,
      products: [],
    }
    context.store.findAll('product')
    .then((products) => {
      this.setState({
        loading: false,
        error: null,
        products,
      })
    })
    .catch((error) => {
      this.setState({
        loading: false,
        error,
      })
    })
  }

  render() {
    const { products } = this.state
    return <ProductList products={products} />
  }
}

ProductListContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}
