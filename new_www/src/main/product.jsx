import React, { PropTypes } from 'react';
import { connect } from 'react-refetch'


class Product extends React.Component {
  render() {
    const { product } = this.props
    return (
      <div>
        <h2>{product.name}</h2>
        <p>{product.description}</p>
        <p>Price: {product.price_rands}</p>
      </div>
    )
  }
}

Product.propTypes = {
  product: PropTypes.object.isRequired,
}


class ProductContainer extends React.Component {
  render() {
    const { productFetch } = this.props
    if (productFetch.pending) {
      return <div>Loading...</div>
    } else if (productFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Product product={productFetch.value} />
    }
  }
}

ProductContainer.propTypes = {
  productFetch: PropTypes.object.isRequired,
}


export default connect((props) => ({
  productFetch: `http://localhost:5000/api/v1/products/${props.params.productId}`,
}))(ProductContainer)
