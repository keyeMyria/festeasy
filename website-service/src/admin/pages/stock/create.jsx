import React, { PropTypes } from 'react'
import { Header, Form, Field, Option, Input, Button } from 'semantic-react'
import MySelect from 'utils/mySelect.jsx'


export default class CreateStockPage extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      products: null,
      selectedProduct: null,
      suppliers: null,
      selectedSupplier: null,
      quantity: '',
      cost: '',
    }
    this.fetchProducts = this.fetchProducts.bind(this)
    this.fetchSuppliers = this.fetchSuppliers.bind(this)
    this.getForm = this.getForm.bind(this)
    this.selectProduct = this.selectProduct.bind(this)
    this.selectSupplier = this.selectSupplier.bind(this)
  }

  componentDidMount() {
    this.fetchProducts()
    this.fetchSuppliers()
  }

  getForm() {
    const {
      products,
      selectedProduct,
      suppliers,
      selectedSupplier,
      quantity,
      cost,
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
        <Form>
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
            />
          </Field>
          <Field label="Cost">
            <Input
              type="number"
              value={cost}
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
