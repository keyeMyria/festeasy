import React from 'react';
import { jsonApiRequest } from '../utils/request.jsx'


const Product = React.createClass({
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


const Store = React.createClass({
  render: function() {
    const productNodes = this.props.products.map(function(product) {
      return (
        <div key={product.id}>
          <Product product={product} />
        </div>
      )
    })
    return (
      <div>
        <h1>Store</h1>
        {productNodes}
      </div>
    )
  }
})


const StoreContainer = React.createClass({
  getInitialState: function() {
    return {
      products: []
    };
  },


  componentDidMount: function() {
    const it = this
    const request = jsonApiRequest('GET', '/products')
    request.then(function(response) {
      return response.json()
    }).then(function(json) {
      it.setState({
        products: json
      })
    })
  },


  render: function() {
    return (
      <div>
        <Store products={this.state.products}/>
      </div>
    )
  }
})


module.exports = StoreContainer
