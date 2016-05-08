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
        <div className="ui items">
          <div className="item">
            <div className="ui small image">
              <img
                className="ui small image"
                src={"/src/images/"+ product.name +".jpg"}/>
            </div>
            <div className="content">
              <a className="header">
                  <h3>
                    {product.name}
                  </h3>
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
