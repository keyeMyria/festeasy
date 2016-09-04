import React, { PropTypes } from 'react'
import Page from 'utils/page.jsx'
import hocProducts from 'common/hocProducts.jsx'
import ProductList from 'main/components/productList.jsx'


class Popular extends React.Component {
  static propTypes = {
    fetchProducts: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts({
      'page-size': 4,
      'order-by': 'created_on',
      'order-direction': 'asc',
    })
  }

  render() {
    const { fetchProductsResponse } = this.props
    const products = fetchProductsResponse.data
    const errors = fetchProductsResponse.errors
    return (
      <div>
        <h2 className="ui header">Popular</h2>
        <Page
          isLoading={!products && !errors}
          content={
            products ? <ProductList products={products} /> : ''
          }
        />
      </div>
    )
  }
}
const WrappedPopular = hocProducts(Popular)


class RecentlyAdded extends React.Component {
  static propTypes = {
    fetchProducts: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts({
      'page-size': 4,
      'order-by': 'created_on',
      'order-direction': 'desc',
    })
  }

  render() {
    const { fetchProductsResponse } = this.props
    const products = fetchProductsResponse.data
    const errors = fetchProductsResponse.errors
    return (
      <div>
        <h2 className="ui header">Recently Added</h2>
        <Page
          isLoading={!products && !errors}
          content={
            products ? <ProductList products={products} /> : ''
          }
        />
      </div>
    )
  }
}
const WrappedRecentlyAdded = hocProducts(RecentlyAdded)


export default class ProductsLandingPage extends React.Component {
  render() {
    return (
      <div>
        <WrappedRecentlyAdded />
        <WrappedPopular />
      </div>
    )
  }
}
