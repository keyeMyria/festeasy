import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { connect } from 'react-refetch'


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


class ProductListContainer extends React.Component {
  render() {
    const { productsFetch } = this.props
    if (productsFetch.pending) {
      return <div>Loading...</div>
    } else if (productsFetch.rejected) {
      return <div>Error</div>
    } else {
      return <ProductList products={productsFetch.value} />
    }
  }
}

ProductListContainer.propTypes = {
  productsFetch: PropTypes.object.isRequired,
}


export default connect(() => ({
  productsFetch: 'http://localhost:5000/api/v1/products',
}))(ProductListContainer)
