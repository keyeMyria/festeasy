import React, { PropTypes } from 'react'
import Page from 'utils/page.jsx'
import genericHOC from 'common/genericHOC.jsx'
import ProductList from 'main/components/productList.jsx'


class CategoryList extends React.Component {
  static propTypes = {
    fetchProducts: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
    params: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts({
      'category': this.props.params.categoryName,
    })
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.params !== this.props.params) {
      this.props.fetchProducts({ category: nextProps.params.categoryName })
    }
  }

  render() {
    const { fetchProductsResponse, params } = this.props
    const products = fetchProductsResponse.data
    const errors = fetchProductsResponse.errors
    return (
      <div>
        <h2 className="ui header">{params.category}</h2>
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

export default genericHOC('Products', 'v1/products')(CategoryList)
