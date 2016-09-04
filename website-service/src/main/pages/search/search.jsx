import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Cards, Breadcrumb } from 'semantic-react'
import ProductCard from 'main/components/productCard.jsx'


class SearchResults extends React.Component {
  static propTypes = {
    products: PropTypes.array.isRequired,
  }

  render() {
    return (
      <div>
        <Breadcrumb>
          <Link className="section" to="/store">All Products</Link>
          <i className="right angle icon divider" />
          Search results
        </Breadcrumb>
        <br />
        <br />
        <Cards className="four">
          {this.props.products.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </Cards>
      </div>
    )
  }
}


export default class SearchContainer extends React.Component {
  static propTypes = {
    location: PropTypes.object.isRequired,
    fetchProducts: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts({
      search: this.props.location.query.term || '',
    })
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.location.query.term !== this.props.location.query.term) {
      this.props.fetchProducts({
        search: nextProps.location.query.term || '',
      })
    }
  }

  render() {
    const { fetchProductsResponse } = this.props
    const products = fetchProductsResponse.data
    const isReady = !!products
    return (
      <div className="ui container">
        {isReady ?
          <SearchResults
            products={products}
          />
        : ''}
      </div>
    )
  }
}
