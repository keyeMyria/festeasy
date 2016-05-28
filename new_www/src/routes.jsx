import React from 'react'
import { Router, Route, browserHistory, IndexRoute } from 'react-router'

import Main from './main/main.jsx'
import StoreContainer from './main/store.jsx'
import Landing from './main/landing.jsx'
import About from './main/about.jsx'
import Festivals from './main/festivals/festivals.jsx'
import Festival from './main/festivals/festival.jsx'
import Product from './main/product.jsx'
import Admin from './admin/admin.jsx'
import App from './app.jsx'
import SignIn from './common/signIn.jsx'
import NotFound from './common/notFound.jsx'


export default (
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <Route path="" component={Main}>
        <IndexRoute component={Landing} />
        <Route path="store" component={StoreContainer} />
        <Route path="products/:productId" component={Product} />
        <Route path="sign-in" component={SignIn} />
        <Route path="about" component={About} />
        <Route path="festivals" component={Festivals} />
        <Route path="festivals/:festivalId" component={Festival} />
      </Route>
      <Route path="admin" component={Admin} />
      <Route path="*" component={NotFound} />
    </Route>
  </Router>
)
