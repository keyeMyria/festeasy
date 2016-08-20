import React, { PropTypes } from 'react';
import Page from 'utils/page.jsx'
import ProductList from './productList.jsx'

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
    const config = { bypassCache: true }
    store.findAll('product', params, config)
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
