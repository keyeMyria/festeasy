import React, { PropTypes } from 'react'


export default function(WrappedComponent) {
  return class extends React.Component {
    static contextTypes = {
      axios: PropTypes.func.isRequired,
    }

    constructor() {
      super()
      this.state = {
        fetchProductsResponse: {
          data: null,
          meta: null,
          errors: null,
          isLoading: false,
        },
      }
      this.fetchProducts = this.fetchProducts.bind(this)
    }

    fetchProducts(queryParams) {
      const state = this.state.fetchProductsResponse
      state.isLoading = true
      this.setState({ fetchProductsResponse: state })
      const request = this.context.axios.get('v1/products', { params: queryParams || {} })
      request.then((response) => {
        state.data = response.data.data
        state.meta = response.data.meta
        state.errors = response.data.errors
        state.isLoading = false
        this.setState({ fetchProductsResponse: state })
      })
      request.catch((response) => {
        state.data = response.data.data
        state.meta = response.data.meta
        state.errors = response.data.errors
        state.isLoading = false
        this.setState({ fetchProductsResponse: state })
      })
      return request
    }

    render() {
      return (
        <WrappedComponent
          {...this.props}
          {...this.state}
          fetchProducts={this.fetchProducts}
        />
      )
    }
  }
}
