import React from 'react'
import { Route, IndexRoute, IndexRedirect } from 'react-router'
import Main from 'admin/index.jsx'
import Landing from 'admin/pages/landing/landing.jsx'
import Stock from 'admin/pages/stock/index.jsx'
import StockList from 'admin/pages/stock/list.jsx'
import CreateStock from 'admin/pages/stock/create.jsx'


export default (
  <Route path="admin" component={Main}>
    <IndexRoute component={Landing} />
    <Route path="stock" component={Stock}>
      <IndexRedirect to="list" />
      <Route path="list" component={StockList} />
      <Route path="create" component={CreateStock} />
    </Route>
  </Route>
)
