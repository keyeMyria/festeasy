import React from 'react'
import { Route, IndexRoute, IndexRedirect } from 'react-router'
import Main from 'admin/index.jsx'
import Landing from 'admin/pages/landing/landing.jsx'
import CreateStock from 'admin/pages/stock/create.jsx'
import ProductList from 'admin/pages/products/list.jsx'
import ProductPage from 'admin/pages/products/product.jsx'
import hocIndexPage from 'admin/utils/HOCIndexPage.jsx'


export default (
  <Route path="admin" component={Main}>
    <IndexRoute component={Landing} />
    <Route
      path="stock"
      component={
        hocIndexPage([{ text: 'Create Stock', url: '/admin/stock/create' }])
      }
    >
      <IndexRedirect to="create" />
      <Route path="create" component={CreateStock} />
    </Route>
    <Route
      path="products"
      component={
        hocIndexPage([{ text: 'Product List', url: '/admin/products/list' }])
      }
    >
      <IndexRedirect to="list" />
      <Route path="list" component={ProductList} />
      <Route path=":productId" component={ProductPage} />
    </Route>
  </Route>
)
