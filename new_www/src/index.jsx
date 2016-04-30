import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'
import { createStore } from 'redux'

import SignInContainer from './common/signIn.jsx'

import Main from './main/main.jsx'
import StoreContainer from './main/store.jsx'
import Landing from './main/landing.jsx'
import About from './main/about.jsx'
import FestivalsContainer from './main/festivals.jsx'
import FestivalContainer from './main/festival.jsx'

import Admin from './admin/admin.jsx'

import appReducer from './utils/reducers.jsx'
import { signIn } from './utils/actionCreators.jsx'


let store = createStore(appReducer)


const App = React.createClass({
  render: function () {
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
