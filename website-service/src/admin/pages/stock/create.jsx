import React, { PropTypes } from 'react'
import { Header, Form, Field, Option, Input, Button } from 'semantic-react'
import MySelect from 'utils/mySelect.jsx'


export default class CreateStockPage extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    axios: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
      products: null,
      selectedProduct: null,
      suppliers: null,
      selectedSupplier: null,
      quantity: '',
      unitCost: '',
    }
    this.fetchProducts = this.fetchProducts.bind(this)
    this.fetchSuppliers = this.fetchSuppliers.bind(this)
    this.getForm = this.getForm.bind(this)
    this.selectProduct = this.selectProduct.bind(this)
    this.selectSupplier = this.selectSupplier.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  componentDidMount() {
    this.fetchProducts()
    this.fetchSuppliers()
  }

  onSubmit(e) {
    e.preventDefault()
    const {
      selectedProduct,
      selectedSupplier,
      unitCost,
      quantity,
    } = this.state
    const data = [...Array(quantity).keys()].map(() => (
      {
        product_id: selectedProduct.id,
        supplier_id: selectedSupplier.id,
        cost_rands: unitCost,
      }
    ))
    this.context.axios({
      method: 'post',
      url: 'v1/stock-units',
      data,
    })
  }

  getForm() {
    const {
      products,
      selectedProduct,
      suppliers,
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
              updateSelected={this.selectProduct}
            />
          </Field>
          <Field label="Supplier">
            <MySelect
              placeholder="Select supplier..."
              selected={selectedSupplier ? [selectedSupplier] : []}
              options={supplierOptions}
              updateSelected={this.selectSupplier}
            />
          </Field>
          <Field label="Quantity">
            <Input
              type="number"
              value={quantity}
              onChange={(e) => this.setState({ quantity: parseInt(e.target.value, 10) })}
            />
          </Field>
          <Field label="Unit Cost">
            <Input
              type="number"
              value={unitCost}
              onChange={(e) => this.setState({ unitCost: e.target.value })}
            />
          </Field>
          <Button>Submit</Button>
        </Form>
      </div>
    )
  }

  selectProduct(products) {
    return new Promise((resolve) => {
      this.setState({ selectedProduct: products[0] }, resolve())
    })
  }

  selectSupplier(suppliers) {
    return new Promise((resolve) => {
      this.setState({ selectedSupplier: suppliers[0] }, resolve())
    })
  }

  fetchSuppliers() {
    this.context.store.findAll('supplier')
    .then((suppliers) => {
      this.setState({ suppliers })
    })
  }

  fetchProducts() {
    this.context.store.findAll('product')
    .then((products) => {
      this.setState({ products })
    })
  }

  render() {
    const { products, suppliers } = this.state
    const isReady = products && suppliers
    return (
      <div>
        {isReady ? this.getForm() : 'loading...' }
      </div>
    )
  }
}
