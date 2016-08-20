import React, { PropTypes } from 'react'
import { Cards } from 'semantic-react'
import ProductCard from 'main/components/productCard.jsx'


class SearchResults extends React.Component {
  static propTypes = {
    products: PropTypes.array.isRequired,
  }

  render() {
    return (
      <Cards className="four">
        {this.props.products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </Cards>
    )
  }
}


export default class SearchContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      products: null,
      festivals: null,
    }
    this.fetchProducts = this.fetchProducts.bind(this)
  }

  componentDidMount() {
    this.fetchProducts()
  }

  componentWillReceiveProps(nextProps) {
    this.fetchProducts({
      search: nextProps.location.query.term,
    })
  }

  fetchProducts(params) {
    this.context.store.findAll(
      'product',
      { search: params ? params.search : this.props.location.query.term || '' },
    )
    .then((products) => {
      this.setState({ products })
    })
  }

  render() {
    const { products } = this.state
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
