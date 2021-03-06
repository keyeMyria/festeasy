import React, { PropTypes } from 'react';
import { Link } from 'react-router'
import { Header, Grid, Column, Breadcrumb, Divider } from 'semantic-react'
import Page from 'utils/page.jsx'
import AddToCartButton from 'main/components/addToCartButton.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'
import ProductImage from 'main/components/productImage.jsx'


class Product extends React.Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
  }

  render() {
    const { product } = this.props
    return (
      <div>
        <Breadcrumb>
          <Link className="section" to="/store">All Products</Link>
          <i className="right angle icon divider" />
          <Link className="section" to={`/store/products/${product.id}`}>
            {product.name}
          </Link>
        </Breadcrumb>
        <br />
        <br />
        <Grid columns={2}>
          <Column width={6}>
            <ProductImage product={product} />
          </Column>
          <Column>
            <Header>{product.name}</Header>
            <p>{product.description}</p>
            <p>Price: <PriceFormatter rands={product.price_rands} /></p>
            <AddToCartButton product={product} />
          </Column>
        </Grid>
        <Divider />
      </div>
    )
  }
}


export default class ProductContainer extends React.Component {
  static contextTypes = {
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      error: null,
      product: null,
    }
  }

  componentDidMount() {
    const { axios } = this.context
    axios.get(`v1/products/${this.props.params.productId}`)
    .then((r) => {
      this.setState({
        product: r.data.data,
        error: null,
      })
    })
    .catch(() => {
      this.setState({
        error: 'Something went wrong',
      })
    })
  }

  render() {
    const { product, error } = this.state
    return (
      <Page
        isLoading={!product && !error}
        contentError={error}
        content={
          product ? <Product product={product} /> : ''
        }
      />
    )
  }
}
