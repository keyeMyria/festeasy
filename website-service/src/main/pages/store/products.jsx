import React, { PropTypes } from 'react'
import { Cards } from 'semantic-react'
import Page from 'utils/page.jsx'
import ProductCard from 'main/components/productCard.jsx'


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


export default class ProductListContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      products: null,
    }
    this.fetchProducts = this.fetchProducts.bind(this)
  }

  componentDidMount() {
    const params = {}
    const searchTerm = this.props.location.query.search
    if (searchTerm) {
      params.search = searchTerm
    }
    this.fetchProducts(params)
  }

  componentWillReceiveProps(nextProps) {
    this.fetchProducts({
      search: nextProps.location.query.search,
    })
  }

  fetchProducts(params) {
    const { store } = this.context
    store.findAll('product', params)
      .then((products) => {
        this.setState({
          loading: false,
          error: null,
          products,
        })
      })
      .catch(() => {
        this.setState({
          loading: false,
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { products, error } = this.state
    return (
      <Page
        isLoading={!products && !error}
        contentError={error}
        content={
          products ? <ProductList products={products} /> : ''
        }
      />
    )
  }
}
