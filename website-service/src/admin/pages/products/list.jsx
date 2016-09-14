import React, { PropTypes } from 'react'
import genericHOC from 'common/genericHOC.jsx'
import DataGridThing from 'common/dataGridThing.jsx'


const ProductListPage = (props, context) => {
  const { fetchProducts, fetchProductsResponse, location } = props
  return (
    <DataGridThing
      queryParams={location.query}
      onQueryPramsChange={q => {
        const newLocation = Object.assign(props.location)
        newLocation.query = Object.assign(newLocation.query, q)
        context.router.push(newLocation)
      }}
      fetchData={fetchProducts}
      fetchDataResponse={fetchProductsResponse}
      headers={[
        { attr: 'id', label: 'Part ID', cellComponent: ({ value }) => <div>Part {value}</div> },
        { attr: 'name', label: 'Name' },
        { attr: 'price_rands', label: 'Price (Rands)' },
      ]}
    />
  )
}

ProductListPage.propTypes = {
  fetchProducts: PropTypes.func.isRequired,
  fetchProductsResponse: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired,
}

ProductListPage.contextTypes = {
  router: PropTypes.object.isRequired,
}


export default genericHOC('Products', 'v1/products')(ProductListPage)
