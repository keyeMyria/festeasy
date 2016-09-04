import React, { PropTypes } from 'react'
import { Header, Form, Field, Option, Input, Button } from 'semantic-react'
import MySelect from 'utils/mySelect.jsx'
import hocProducts from 'common/hocProducts.jsx'
import hocSuppliers from 'common/hocSuppliers.jsx'


class CreateStockUnitForm extends React.Component {
  static propTypes = {
    products: PropTypes.array.isRequired,
    suppliers: PropTypes.array.isRequired,
  }

  constructor() {
    super()
    this.state = {
      selectedProduct: null,
      selectedSupplier: null,
      quantity: 1,
      unitCost: '',
    }
    this.onSubmit = this.onSubmit.bind(this)
  }

  onSubmit(e) {
    e.preventDefault()
    const { selectedProduct, selectedSupplier, quantity, unitCost } = this.state
    this.props.createStockUnit({
      product_id: selectedProduct.id,
      supplier_id: selectedSupplier.id,
      quantity,
      cost_rands: unitCost,
    })
  }

  render() {
    const {
      products,
      suppliers,
    } = this.props
    const {
      selectedProduct,
      selectedSupplier,
      quantity,
      unitCost,
    } = this.state
    const productOptions = products.map((p) => (
      <Option key={p.id} value={p}>
        {p.name}
      </Option>
    ))
    const supplierOptions = suppliers.map((s) => (
      <Option key={s.id} value={s}>
        {s.name}
      </Option>
    ))
    return (
      <div>
        <Header>Create Stock Unit</Header>
        <Form onSubmit={this.onSubmit}>
          <Field label="Product">
            <MySelect
              placeholder="Select product..."
              selected={selectedProduct ? [selectedProduct] : []}
              options={productOptions}
              updateSelected={ps => this.setState({ selectedProduct: ps[0] })}
            />
          </Field>
          <Field label="Supplier">
            <MySelect
              placeholder="Select supplier..."
              selected={selectedSupplier ? [selectedSupplier] : []}
              options={supplierOptions}
              updateSelected={ss => this.setState({ selectedSupplier: ss[0] })}
            />
          </Field>
          <Field label="Quantity">
            <Input
              type="number"
              min={1}
              max={10}
              value={quantity || ''}
              onChange={(e) => this.setState({ quantity: parseInt(e.target.value, 10) })}
              required
            />
          </Field>
          <Field label="Unit Cost (Rands)">
            <Input
              type="number"
              min={0}
              value={unitCost || ''}
              onChange={(e) => this.setState({ unitCost: e.target.value })}
              required
            />
          </Field>
          <Button>Submit</Button>
        </Form>
      </div>
    )
  }
}


class CreateStockPage extends React.Component {
  static propTypes = {
    fetchProducts: PropTypes.func.isRequired,
    fetchSuppliers: PropTypes.func.isRequired,
    fetchProductsResponse: PropTypes.object.isRequired,
    fetchSuppliersResponse: PropTypes.object.isRequired,
  }

  componentDidMount() {
    this.props.fetchProducts()
    this.props.fetchSuppliers()
  }

  render() {
    const { fetchProductsResponse, fetchSuppliersResponse } = this.props
    const isReady = fetchProductsResponse.data && fetchSuppliersResponse.data
    return (
      <div>
        {isReady ?
          <CreateStockUnitForm
            products={fetchProductsResponse.data}
            suppliers={fetchSuppliersResponse.data}
          /> : ''}
      </div>
    )
  }
}


export default hocProducts(hocSuppliers(CreateStockPage))
