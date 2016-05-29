module.exports = [
  {
    name: 'cart',
    endpoint: 'carts',
    relations: {
      hasMany: {
        cartProduct: {
          localField: 'cart_products',
          foreignKey: 'cart_id',
        },
      },
    },
  },
  {
    name: 'cartProduct',
    endpoint: 'cart-products',
    relations: {
      belongsTo: {
        cart: {
          localField: 'cart',
          localKey: 'cart_id',
        },
      },
    },
  },
  {
    name: 'product',
    endpoint: 'products',
  },
  {
    name: 'festival',
    endpoint: 'festivals',
  },
]
