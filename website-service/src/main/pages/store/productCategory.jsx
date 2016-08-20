import React, { PropTypes } from 'react';
import Page from 'utils/page.jsx'
import ProductList from './productList.jsx'


export default class ProductCategoryContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      prod: null,
      cat: null,
    }
  }

  componentWillReceiveProps(props) {
    console.log('gettingprops: ', props.params.category)
    this.setState({
      cat: props.params.category,
    }, this.getProducts)
  }

  getProducts() {
    const { store } = this.context
    store.findAll('product', { 'category': this.state.cat }, { bypassCache: true })
      .then((prod) => {
        this.setState({
          prod,
          error: null,
        })
      })
      .catch(() => {
        this.setState({
          error: 'Something went wrong',
        })
      })
  }

  componentDidMount() {
    this.getProducts()
  }

  render() {
    const { prod, error } = this.state
    console.log('cats: ', prod)
    return (
      <Page
        isLoading={!prod && !error}
        contentError={error}
        content={
          prod ? <ProductList products={prod} /> : ''
        }
      />
    )
  }
}
