import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import {
  Image,
  Card,
  Content,
  Header,
  Description,
} from 'semantic-react'
import AddToCartButton from 'main/components/addToCartButton.jsx'
import PriceFormatter from 'utils/priceFormatter.jsx'
import apiEndpoint from 'apiEndpoint.js'


export default class ProductCard extends React.Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
  }

  render() {
    const { product } = this.props
    const imageHeight = '200'
    return (
      <Card>
        <Link to={`/store/products/${product.id}`}>
          <div style={{ minHeight: imageHeight }}>
            {product.thumbnail_image_id ?
              <Image
                centered
                style={{ maxHeight: imageHeight, width: 'auto', height: 'auto' }}
                alt="product thumbnail"
                src={apiEndpoint.concat(
                  `v1/images/${product.thumbnail_image_id}/image?height=${imageHeight}`
                )}
              /> : 'No thumbnail image'
            }
          </div>
        </Link>
        <Content>
          <Header>
            <Link to={`/store/products/${product.id}`}>
              {product.name}
            </Link>
          </Header>
          <Description>{product.description}</Description>
          <PriceFormatter rands={product.price_rands} />
        </Content>
        <Content extra>
          <AddToCartButton product={product} />
        </Content>
      </Card>
    )
  }
}
