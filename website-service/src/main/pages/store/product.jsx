import React, { PropTypes } from 'react';
import { Link } from 'react-router'
import { Header, Image, Grid, Column, Breadcrumb } from 'semantic-react'
import Page from 'utils/page.jsx'
import AddToCartButton from 'main/components/addToCartButton.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'
import apiEndpoint from 'apiEndpoint.js'


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
          <Column width={4}>
            {product.thumbnail_image_id ?
              <Image
                centered
                style={{ maxHeight: '270px', width: 'auto', height: 'auto' }}
                alt="product thumbnail"
                src={apiEndpoint.concat(`v1/images/${product.thumbnail_image_id}/image`)}
              /> : 'No thumbnail image'
            }
          </Column>
          <Column>
            <Header>{product.name}</Header>
            <p>{product.description}</p>
            <p>Price: <PriceFormatter rands={product.price_rands} /></p>
            <AddToCartButton product={product} />
          </Column>
        </Grid>
      </div>
    )
  }
}


export default class ProductContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
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
    const { store } = this.context
    store.find('product', this.props.params.productId, { bypassCache: true })
      .then((product) => {
        this.setState({
          product,
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
