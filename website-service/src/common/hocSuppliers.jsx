import React, { PropTypes } from 'react'


export default function(WrappedComponent) {
  return class extends React.Component {
    static contextTypes = {
      axios: PropTypes.func.isRequired,
    }

    constructor() {
      super()
      this.state = {
        fetchSuppliersResponse: {
          data: null,
          meta: null,
          errors: null,
          isLoading: false,
        },
      }
      this.fetchSuppliers = this.fetchSuppliers.bind(this)
    }

    fetchSuppliers(queryParams) {
      const state = this.state.fetchSuppliersResponse
      state.isLoading = true
      this.setState({ fetchSuppliersResponse: state })
      const request = this.context.axios.get('v1/suppliers', { params: queryParams || {} })
      request.then((response) => {
        state.data = response.data.data
        state.meta = response.data.meta
        state.errors = response.data.errors
        state.isLoading = false
        this.setState({ fetchSuppliersResponse: state })
      })
      request.catch((response) => {
        state.data = response.data.data
        state.meta = response.data.meta
        state.errors = response.data.errors
        state.isLoading = false
        this.setState({ fetchSuppliersResponse: state })
      })
      return request
    }

    render() {
      return (
        <WrappedComponent
          {...this.props}
          {...this.state}
          fetchSuppliers={this.fetchSuppliers}
        />
      )
    }
  }
}
