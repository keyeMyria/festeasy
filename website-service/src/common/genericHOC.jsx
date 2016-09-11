import React, { PropTypes } from 'react'


export default function(resourceName, endpoint) {
  const fetchResourceName = `fetch${resourceName}Response`
  return function(WrappedComponent) {
    return class extends React.Component {
      static contextTypes = {
        axios: PropTypes.func.isRequired,
      }

      constructor() {
        super()
        this.state = {
          [fetchResourceName]: {
            data: null,
            meta: null,
            errors: null,
            isLoading: false,
          },
        }
      }

      fetchCollection = (queryParams) => {
        const state = this.state[fetchResourceName]
        state.isLoading = true
        this.setState({ [fetchResourceName]: state })
        const request = this.context.axios.get(endpoint, { params: queryParams || {} })
        request.then((response) => {
          state.data = response.data.data
          state.meta = response.data.meta
          state.errors = response.data.errors
          state.isLoading = false
          this.setState({ [fetchResourceName]: state })
        })
        request.catch((response) => {
          state.data = response.data.data
          state.meta = response.data.meta
          state.errors = response.data.errors
          state.isLoading = false
          this.setState({ [fetchResourceName]: state })
        })
        return request
      }

      render() {
        const funcs = { [`fetch${resourceName}`]: this.fetchCollection }
        return (
          <WrappedComponent
            {...this.props}
            {...this.state}
            {...funcs}
          />
        )
      }
    }
  }
}
