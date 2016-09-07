import React, { Component } from 'react'
import hocProducts from 'common/hocProducts.jsx'


class ProductsPage extends Component {
  render() {
    return (
      <div>
        Products here
      </div>
    )
  }
}


export default hocProducts(ProductsPage)
