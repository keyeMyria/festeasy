import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'
import thunkMiddleware from 'redux-thunk'
import createLogger from 'redux-logger'
import { createStore, applyMiddleware } from 'redux'


import rootReducer from './utils/reducers.jsx'
import SignInContainer from './common/signIn.jsx'
import Main from './main/main.jsx'
import StoreContainer from './main/store.jsx'
import Landing from './main/landing.jsx'
import About from './main/about.jsx'
import FestivalsContainer from './main/festivals/festivals.jsx'
import FestivalContainer from './main/festivals/festival.jsx'
import CartContainer from './main/cart.jsx'
import Admin from './admin/admin.jsx'
import { fetchFestivals } from './utils/actions.jsx'


const loggerMiddleware = createLogger()

let store = createStore(
  rootReducer,
  applyMiddleware(
    thunkMiddleware,
    loggerMiddleware
  )
)

store.dispatch(fetchFestivals())


const App = React.createClass({
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
        <Route path="about" component={About}/>
        <Route path="cart" component={CartContainer}/>
        <Route path="festivals" component={FestivalsContainer}/>
        <Route path="festivals/:festivalId" component={FestivalContainer}/>
      </Route>
      <Route path="admin" component={Admin}/>
    </Route>
  </Router>


ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
