import React, { PropTypes, Component } from 'react'
import { Loader } from 'utils/loader.jsx'
import { Error } from 'utils/error.jsx'
import { BasicForm } from 'utils/form.jsx'


export default class ProductPage extends Component {
  static contextTypes = {
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      fetchProductResponse: {
        data: null,
        errors: null,
        meta: null,
        isLoading: false,
      },
      updateProductResponse: {
        data: null,
        errors: null,
        meta: null,
        isLoading: false,
      },
    }
  }

  componentDidMount() {
    this.fetchProduct()
  }

  fetchProduct = () => {
    const { productId } = this.props.params
    const state = Object.assign(this.state.fetchProductResponse)
    state.isLoading = true
    this.setState({ fetchProductResponse: state })
    this.context.axios.get(`v1/products/${productId}`)
    .then((r) => {
      state.isLoading = false
      state.data = r.data.data
      state.errors = null
      state.meta = r.data.meta
      this.setState({ fetchProductResponse: state })
    })
    .catch((r) => {
      state.isLoading = false
      state.data = r.data.data
      state.errors = null
      state.meta = r.data.meta
      this.setState({ fetchProductResponse: state })
    })
  }

  handleSubmit = formData => {
    const { productId } = this.props.params
    const updateState = Object.assign(this.state.updateProductResponse)
    updateState.isLoading = true
    this.setState({ updateProductResponse: updateState })
    // TODO: Why does returning axios.patch do what I want in BasicForm.
    return new Promise((resolve, reject) => (
      this.context.axios.patch(`v1/products/${productId}`, formData)
      .then((r) => {
        updateState.isLoading = false
        updateState.data = r.data.data
        updateState.errors = null
        updateState.meta = r.data.meta
        this.setState({ updateProductResponse: updateState })
        resolve(r)
      })
      .catch((r) => {
        updateState.isLoading = false
        updateState.errors = r.data ? r.data.errors : []
        this.setState({ updateProductResponse: updateState })
        reject(r)
      })
    ))
  }

  render() {
    let result = <Loader />
    const { fetchProductResponse, updateProductResponse } = this.state
    if (fetchProductResponse.errors) {
      result = <Error />
    } else if (updateProductResponse.data || fetchProductResponse.data) {
      const p = updateProductResponse.data ? updateProductResponse.data : fetchProductResponse.data
      result = (
        <BasicForm
          onSubmit={this.handleSubmit}
          isLoading={updateProductResponse.isLoading}
          fields={[
            {
              attr: 'name',
              label: 'Name',
              initialValue: p.name,
            },
            {
              attr: 'description',
              label: 'Description',
              initialValue: p.description,
            },
            {
              attr: 'price_rands',
              label: 'Price (Rands)',
              initialValue: p.price_rands,
            },
          ]}
        />
      )
    }
    return result
  }
}
