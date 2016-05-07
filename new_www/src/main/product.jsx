import React, { PropTypes } from 'react';
import { connect } from 'react-refetch'
import AddToCartButton from './addToCartButton.jsx'
import { productShape } from '../utils/shapes.jsx'


const Product = React.createClass({
  propTypes: {
    product: productShape.isRequired,
  },

  render: function() {
    const { product } = this.props
    return (
      <div>
        <h2>{product.name}</h2>
        <p>{product.description}</p>
        <p>Price: {product.price_rands}</p>
        <AddToCartButton productId={product.id} />
      </div>
    )
  },
})


const ProductContainer = React.createClass({
  propTypes: {
    productFetch: PropTypes.object.isRequired,
  },

  render: function() {
    const { productFetch } = this.props
    if (productFetch.pending) {
      return <div>Loading...</div>
    } else if (productFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Product product={productFetch.value} />
    }
  },
})


export default connect((props) => ({
  productFetch: `http://localhost:5000/api/v1/products/${props.params.productId}`,
}))(ProductContainer)
