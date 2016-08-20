module.exports = [
  {
    name: 'stockUnit',
    endpoint: 'v1/stock-units',
  },
  {
    name: 'supplier',
    endpoint: 'v1/suppliers',
  },
  {
    name: 'cart',
    endpoint: 'v1/carts',
  },
  {
    name: 'cartProduct',
    endpoint: 'v1/cart-products',
  },
  {
    name: 'product',
    endpoint: 'v1/products',
    maxAge: 60000,
  },
  {
    name: 'payu-transaction',
    endpoint: 'v1/payu-transactions',
  },
  {
    name: 'festival',
    endpoint: 'v1/festivals',
    maxAge: 60000,
  },
  {
    name: 'order',
    endpoint: 'v1/orders',
  },
  {
    name: 'user',
    endpoint: 'v1/users',
  },
  {
    name: 'invoice',
    endpoint: 'v1/invoices',
  },
  {
    name: 'invoiceProduct',
    endpoint: 'v1/invoice-products',
  },
  {
    name: 'forgotPasswordToken',
    endpoint: 'v1/forgot-password-tokens',
  },
]
