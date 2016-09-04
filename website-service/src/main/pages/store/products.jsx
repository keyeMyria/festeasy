import React, { PropTypes } from 'react'
import { Cards } from 'semantic-react'
import Page from 'utils/page.jsx'
import ProductCard from 'main/components/productCard.jsx'
import hocProducts from 'common/hocProducts.jsx'


class ProductList extends React.Component {
  static propTypes = {
    products: PropTypes.arrayOf(
      PropTypes.object
    ).isRequired,
  }

  render() {
    const { products } = this.props
    let result
    if (products.length === 0) {
      result = <div>No results</div>
    } else {
      result = (
        <Cards className="four">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </Cards>
      )
    }
    return result
  }
}


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


export default class ProductsPage extends React.Component {
  render() {
    return (
      <div>
        <WrappedRecentlyAdded />
        <WrappedPopular />
      </div>
    )
  }
}
