import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { Items, Item, Header, Description, Meta } from 'semantic-react'
import AddToCartButton from 'main/components/addToCartButton.jsx'
import Page from 'utils/page.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'


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
        <Items divided relaxed>
          {products.map(product => (
            <Item key={product.id}>
              <Header>
                <Link to={`/store/products/${product.id}`}>
                  {product.name}
                </Link>
              </Header>
              <Meta>Description</Meta>
              <Description>{product.description}</Description>
              <p>Price: <PriceFormatter rands={product.price_rands} /></p>
              <AddToCartButton product={product} />
            </Item>
          ))}
        </Items>
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
