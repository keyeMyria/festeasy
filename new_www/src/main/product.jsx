import React, { PropTypes } from 'react';


class Product extends React.Component {
  render() {
    const { product } = this.props
    return (
      <div>
        <h2>{product.name}</h2>
        <p>{product.description}</p>
        <p>Price: {product.price_rands}</p>
      </div>
    )
  }
}

Product.propTypes = {
  product: PropTypes.object.isRequired,
}


export default class ProductContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: false,
      error: null,
      product: null,
    }
  }

  componentWillMount() {
    this.context.store.find('product', this.props.params.productId)
    .then((product) => {
      this.setState({
        loading: false,
        error: null,
        product,
      })
    })
    .catch((error) => {
      this.setState({
        loading: false,
        error,
      })
    })
  }

  render() {
    const { product, error } = this.state
    if (product) {
      return <Product product={product} />
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading...</div>
    }
  }
}

ProductContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}

ProductContainer.propTypes = {
  params: PropTypes.object.isRequired,
}
