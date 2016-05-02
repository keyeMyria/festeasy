import React, { PropTypes } from 'react';
import { connect, PromiseState } from 'react-refetch'


const ProductListItem = React.createClass({
  propTypes: {
    product: PropTypes.shape({
      id: PropTypes.number.isRequired
      })
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
  render: function() {
    const { productsFetch } = this.props
    var productNodes;
    if (productsFetch.value) {
      productNodes = productsFetch.value.map(function(product) {
        return <ProductListItem key={product.id} product={product} />
      })
    }
    return (
      <div>
        <h1>Store</h1>
        {productNodes}
      </div>
    )
  }
})


const StoreContainer = connect(props => ({
  productsFetch: 'http://localhost:5000/api/v1/products'
}))(ProductList)


module.exports = StoreContainer
