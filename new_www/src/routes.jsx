import React from 'react'
import { Router, Route, browserHistory, IndexRoute } from 'react-router'

import Main from './main/main.jsx'
import Store from './main/pages/store.jsx'
import Landing from './main/pages/landing.jsx'
import About from './main/pages/about.jsx'
import Festivals from './main/pages/festivals.jsx'
import Festival from './main/pages/festival.jsx'
import Product from './main/pages/product.jsx'
import Admin from './admin/admin.jsx'
import App from './app.jsx'
import SignIn from './common/signIn.jsx'
import SignUp from './common/signUp.jsx'
import NotFound from './common/notFound.jsx'
import Cart from './main/pages/cart.jsx'
import Checkout from './main/pages/checkout/checkout.jsx'
import Review from './main/pages/checkout/review.jsx'
import Payment from './main/pages/checkout/payment.jsx'
import PaymentCancellation from './main/pages/paymentCancellation.jsx'
import PaymentConfirmation from './main/pages/paymentConfirmation.jsx'
import Account from './main/pages/account.jsx'
import Orders from './main/pages/orders.jsx'
import Settings from './main/pages/settings.jsx'


export default (
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <Route path="" component={Main}>
        <IndexRoute component={Landing} />
        <Route path="store" component={Store} />
        <Route path="products/:productId" component={Product} />
        <Route path="sign-up" component={SignUp} />
        <Route path="sign-in" component={SignIn} />
        <Route path="payment-confirmation" component={PaymentConfirmation} />
        <Route path="payment-cancellation" component={PaymentCancellation} />
        <Route path="account" component={Account}>
          <Route path="orders" component={Orders} />
          <Route path="settings" component={Settings} />
        </Route>
        <Route path="cart" component={Cart} />
        <Route path="checkout" component={Checkout}>
          <Route path="review" component={Review} />
          <Route path="payment" component={Payment} />
        </Route>
        <Route path="about" component={About} />
        <Route path="festivals" component={Festivals} />
        <Route path="festivals/:festivalId" component={Festival} />
      </Route>
      <Route path="admin" component={Admin} />
      <Route path="*" component={NotFound} />
    </Route>
  </Router>
)
