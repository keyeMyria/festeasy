import React, { PropTypes, Component } from 'react'
import genericHOC from 'common/genericHOC.jsx'
import { BasicTable } from 'utils/table.jsx'
import { Loader } from 'utils/loader.jsx'
import { Error } from 'utils/error.jsx'


class ProductsPage extends Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    fetchProducts: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts()
  }

  render() {
    let result = <Loader />
    const { fetchProductsResponse } = this.props
    if (fetchProductsResponse.errors) {
      result = <Error />
    } else if (fetchProductsResponse.data) {
      result = (
        <BasicTable
          componentProps={{ selectable: true }}
          onRowClick={r => this.context.router.push(`/admin/products/${r.id}`)}
          headers={[
            { attr: 'id', label: 'Part ID' },
            { attr: 'name', label: 'Name' },
            { attr: 'price_rands', label: 'Price (Rands)' },
          ]}
          rows={this.props.fetchProductsResponse.data}
        />
      )
    }
    return result
  }
}


export default genericHOC('Products', 'v1/products')(ProductsPage)
