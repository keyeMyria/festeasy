import React, { PropTypes } from 'react';
import { connect, PromiseState } from 'react-refetch'


const productShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  price_rands: PropTypes.number.isRequired
})


const ProductListItem = React.createClass({
  propTypes: {
    product: productShape.isRequired
  },


  render: function() {
    return (
      <div>
        <h3>{this.props.product.name}</h3>
        <p>{this.props.product.description}</p>
        <p>Price: {this.props.product.price_rands}</p>
      </div>
    )
  }
})


const ProductList = React.createClass({
  propTypes: {
    products: PropTypes.arrayOf(
      productShape
    ).isRequired
  },


  render: function() {
    const { products } = this.props
    return (
      <div>
        <h1>Store</h1>
        {products.map(product => (
          <ProductListItem key={product.id} product={product}/>
        ))}
      </div>
    )
  }
})


const ProductListContainer = React.createClass({
  render: function() {
    const { productsFetch } = this.props
    if (productsFetch.pending) {
      return <div>Loading...</div>
    } else if (productsFetch.rejected) {
      return <div>Error</div>
    } else {
      return <ProductList products={productsFetch.value}/>
    }
  }
})


export default connect(props => ({
  productsFetch: 'http://localhost:5000/api/v1/products'
}))(ProductListContainer)
