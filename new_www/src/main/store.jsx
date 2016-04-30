import React from 'react';


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
    this.serverRequest = $.get('http://localhost:5000/api/v1/products', function(result) {
      this.setState({
        products: result
      })
    }.bind(this))
  },


  componentWillUnmount: function() {
    this.serverRequest.abort();
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
