import React, { PropTypes, Component } from 'react'
import { Image } from 'semantic-react'
import apiEndpoint from 'apiEndpoint.js'


export default class ProductImage extends Component {
  static propTypes = {
    product: PropTypes.object.isRequired,
    maxHeight: PropTypes.number.isRequired,
  }

  static defaultProps = {
    maxHeight: 250,
  }

  render() {
    const { product, maxHeight } = this.props
    return (
      <div>
        {product.thumbnail_image_id ?
          <Image
            centered
            style={{ 'maxHeight': `${maxHeight}px` }}
            alt="product thumbnail"
            src={apiEndpoint.concat(`v1/images/${product.thumbnail_image_id}/image`)}
          /> : 'No thumbnail image'
        }
      </div>
    )
  }
}
