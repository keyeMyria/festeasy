import React, { PropTypes, Component } from 'react'
import { Option } from 'semantic-react'
import genericHOC from 'common/genericHOC.jsx'
import { Loader } from 'utils/loader.jsx'
import { Error } from 'utils/error.jsx'
import { BasicForm } from 'utils/form.jsx'
import { MultiSelect } from 'utils/select.jsx'


class ProductPage extends Component {
  static contextTypes = {
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
    fetchCategories: PropTypes.func.isRequired,
    fetchCategoriesResponse: PropTypes.object.isRequired,
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
    this.props.fetchCategories({ 'product-id': this.props.params.productId })
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
      state.errors = r.data ? r.data.errors : []
      this.setState({ fetchProductResponse: state })
    })
  }

  handleSubmit = formData => {
    console.log(formData)
    const { productId } = this.props.params
    const state = Object.assign(this.state.updateProductResponse)
    state.isLoading = true
    this.setState({ updateProductResponse: state })
    // TODO: Why does returning axios.patch do what I want in BasicForm.
    return new Promise((resolve, reject) => (
      this.context.axios.patch(`v1/products/${productId}`, formData)
      .then((r) => {
        state.isLoading = false
        state.data = r.data.data
        state.errors = null
        state.meta = r.data.meta
        this.setState({ updateProductResponse: state })
        resolve(r)
      })
      .catch((r) => {
        state.isLoading = false
        state.errors = r.data ? r.data.errors : []
        this.setState({ updateProductResponse: state })
        reject(r)
      })
    ))
  }

  render() {
    let result = <Loader />
    const { fetchCategoriesResponse } = this.props
    const { fetchProductResponse, updateProductResponse } = this.state
    if (fetchProductResponse.errors) {
      result = <Error />
    } else if (
      (updateProductResponse.data || fetchProductResponse.data) && fetchCategoriesResponse.data
    ) {
      const p = updateProductResponse.data ? updateProductResponse.data : fetchProductResponse.data
      const categories = fetchCategoriesResponse.data
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
            {
              attr: 'categories',
              label: 'Categories',
              component: MultiSelect,
              componentProps: {
                placeholder: 'Select categories...',
                props: {
                  search: true,
                },
                options: categories.map((c) => (
                  <Option key={c.id} value={c}>{c.name}</Option>
                )),
              },
            },
          ]}
        />
      )
    }
    return result
  }
}


export default genericHOC('Categories', 'v1/categories')(
  genericHOC('Product', 'v1/products')(
    ProductPage
  )
)
