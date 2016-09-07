import React, { PropTypes } from 'react'
import { Option } from 'semantic-react'
import hocProducts from 'common/hocProducts.jsx'
import hocSuppliers from 'common/hocSuppliers.jsx'
import { BasicForm } from 'utils/form.jsx'
import { SingleSelect } from 'utils/select.jsx'


class CreateStockUnitForm extends React.Component {
  static propTypes = {
    products: PropTypes.array.isRequired,
    suppliers: PropTypes.array.isRequired,
  }

  render() {
    const { products, suppliers } = this.props
    return (
      <div>
        <BasicForm
          onSubmit={data => console.log(data)}
          header="Create Stock Unit"
          fields={[
            {
              attr: 'selectedProduct',
              label: 'Product',
              component: SingleSelect,
              componentProps: {
                placeholder: 'Select product...',
                props: {
                  search: true,
                },
                options: products.map((p) => (
                  <Option key={p.id} value={p}>{p.name}</Option>
                )),
              },
            },
            {
              attr: 'selectedSupplier',
              label: 'Supplier',
              component: SingleSelect,
              componentProps: {
                placeholder: 'Select supplier...',
                props: {
                  search: true,
                },
                options: suppliers.map((s) => (
                <Option key={s.id} value={s}>{s.name}</Option>
                )),
              },
            },
            {
              attr: 'quantity',
              label: 'Quantity',
              props: {
                type: 'number',
              },
            },
            {
              attr: 'unit_cost',
              label: 'Unit Cost (Rands)',
              props: {
                type: 'number',
              },
            },
          ]}
        />
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
