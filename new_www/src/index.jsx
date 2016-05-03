import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router'

import SignInContainer from './common/signIn.jsx'
import Main from './main/main.jsx'
import StoreContainer from './main/store.jsx'
import Landing from './main/landing.jsx'
import About from './main/about.jsx'
import Festivals from './main/festivals/festivals.jsx'
import Festival from './main/festivals/festival.jsx'
import Cart from './main/cart.jsx'
import Product from './main/product.jsx'
import Admin from './admin/admin.jsx'
import auth from './utils/auth.jsx'


const App = React.createClass({
  propTypes: {
    children: PropTypes.object.isRequired
  },


  childContextTypes: {
      isSignedIn: PropTypes.bool.isRequired
  },


  getChildContext: function() {
    return {isSignedIn: this.state.signedIn};
  },


  getInitialState() {
    return {
      signedIn: auth.signedIn()
    }
  },


  updateAuth(signedIn) {
    this.setState({
      signedIn: !!signedIn
    })
  },


  componentWillMount() {
    auth.onChange = this.updateAuth
    auth.signIn()
  },

  render: function() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
})


const routes =
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <Route path="" component={Main}>
        <IndexRoute component={Landing}/>
        <Route path="sign-in" component={SignInContainer}/>
        <Route path="store" component={StoreContainer}/>
        <Route path="products/:productId" component={Product}/>
        <Route path="about" component={About}/>
        <Route path="cart" component={Cart}/>
        <Route path="festivals" component={Festivals}/>
        <Route path="festivals/:festivalId" component={Festival}/>
      </Route>
      <Route path="admin" component={Admin}/>
    </Route>
  </Router>


ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
