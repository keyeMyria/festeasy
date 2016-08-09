import React from 'react'
import { Route, IndexRoute, IndexRedirect } from 'react-router'
import Main from 'main/index.jsx'
import Store from 'main/pages/store/store.jsx'
import Products from 'main/pages/store/products.jsx'
import Landing from 'main/pages/landing/landing.jsx'
import About from 'main/pages/about/about.jsx'
import FestivalList from 'main/pages/festivals/festivalList.jsx'
import Festivals from 'main/pages/festivals/festivals.jsx'
import Festival from 'main/pages/festivals/festival.jsx'
import Product from 'main/pages/store/product.jsx'
import SignIn from 'main/pages/signIn.jsx'
import SignUp from 'main/pages/signUp.jsx'
import Cart from 'main/pages/cart/cart.jsx'
import Checkout from 'main/pages/checkout/checkout.jsx'
import Review from 'main/pages/checkout/review.jsx'
import Payment from 'main/pages/checkout/payment.jsx'
import PaymentCancellation from 'main/pages/paymentRedirects/paymentCancellation.jsx'
import PaymentConfirmation from 'main/pages/paymentRedirects/paymentConfirmation.jsx'
import Account from 'main/pages/account/account.jsx'
import Orders from 'main/pages/account/orders.jsx'
import Settings from 'main/pages/account/settings.jsx'
import Invoice from 'main/pages/account/invoice.jsx'
import RecoverPassword from 'main/pages/recoverPassword.jsx'


export default (
  <Route path="" component={Main}>
    <IndexRoute component={Landing} />
    <Route path="store" component={Store}>
      <IndexRoute component={Products} />
      <Route path="products/:productId" component={Product} />
    </Route>
    <Route path="sign-up" component={SignUp} />
    <Route path="sign-in" component={SignIn} />
    <Route path="recover-password" component={RecoverPassword} />
    <Route path="payment-confirmation" component={PaymentConfirmation} />
    <Route path="payment-cancellation" component={PaymentCancellation} />
    <Route path="account" component={Account}>
      <IndexRedirect to="orders" />
      <Route path="orders" component={Orders} />
      <Route path="orders/:orderId/invoice" component={Invoice} />
      <Route path="settings" component={Settings} />
    </Route>
    <Route path="cart" component={Cart} />
    <Route path="checkout" component={Checkout}>
      <Route path="review" component={Review} />
      <Route path="payment" component={Payment} />
    </Route>
    <Route path="about" component={About} />
    <Route path="festivals" component={Festivals}>
      <IndexRoute component={FestivalList} />
      <Route path=":festivalId" component={Festival} />
    </Route>
  </Route>
)
