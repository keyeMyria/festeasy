import React, { PropTypes } from 'react'
import { Cards } from 'semantic-react'
import ProductCard from 'main/components/productCard.jsx'


export default class ProductList extends React.Component {
  static propTypes = {
    products: PropTypes.arrayOf(
      PropTypes.object
    ).isRequired,
  }

  render() {
    const { products } = this.props
    let result
    if (products.length === 0) {
      result = <div>No results</div>
    } else {
      result = (
        <Cards className="four">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </Cards>
      )
    }
    return result
  }
}
