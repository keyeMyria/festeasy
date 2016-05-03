import { PropTypes } from 'react'


const productShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  price_rands: PropTypes.number.isRequired
})


const cartShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  total_rands: PropTypes.number.isRequired,
  festival: PropTypes.object,
  cart_products: PropTypes.oneOfType([
    PropTypes.array,
    cartProductShape
  ]).isRequired
})


const cartProductShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  'product_id': PropTypes.number.isRequired,
  product: PropTypes.object.isRequired
})


const festivalShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  starts_on: PropTypes.string.isRequired,
  ends_on: PropTypes.string.isRequired
})


module.exports = {
  cartProductShape,
  festivalShape,
  cartShape,
  productShape
}
