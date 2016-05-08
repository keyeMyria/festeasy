import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { connect } from 'react-refetch'
import 'whatwg-fetch';
import AddToCartButton from './addToCartButton.jsx'
import { productShape } from '../utils/shapes.jsx'


const ProductListItem = React.createClass({
  propTypes: {
    product: productShape.isRequired,
  },
  render: function() {
    const { product } = this.props
    return (
      <div>
        <div className="ui items">
          <div className="item">
            <div className="ui small image">
              <img
                role="presentation"
                className="ui small image"
                src={"/src/images/"+ product.name +".jpg"}/>
            </div>
            <div className="content">
              <a className="header">
                <Link to={`/products/${product.id}`}>
                  <h3>
                    {product.name}
                  </h3>
                </Link>
              </a>
              <div className="meta">
                <span>
                  Price: {product.price_rands}
                </span>
              </div>
              <div className="description">
                <p>
                    {product.description}
                </p>
              </div>
              <div className="extra">
                <AddToCartButton productId={product.id} />
              </div>
            </div>
          </div>
        </div>
        <div className="ui divider"></div>
      </div>
    )
  },
})


const ProductList = React.createClass({
  propTypes: {
    products: PropTypes.arrayOf(
      productShape
    ).isRequired,
  },

  render: function() {
    const { products } = this.props
    return (
      <div>
        <h1>Store</h1>
        {products.map(product => (
          <ProductListItem key={product.id} product={product} />
        ))}
      </div>
    )
  },
})


const ProductListContainer = React.createClass({
  propTypes: {
    productsFetch: PropTypes.object.isRequired,
  },

  render: function() {
    const { productsFetch } = this.props
    if (productsFetch.pending) {
      return <div>Loading...</div>
    } else if (productsFetch.rejected) {
      return <div>Error</div>
    } else {
      return <ProductList products={productsFetch.value} />
    }
  },
})


export default connect(() => ({
  productsFetch: 'http://localhost:5000/api/v1/products',
}))(ProductListContainer)
