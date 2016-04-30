import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'

import Store from './store/store.jsx'
import Landing from './store/landing.jsx'
import About from './store/about.jsx'
import FestivalsContainer from './store/festivals.jsx'

import Admin from './admin/admin.jsx'


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
      <Route path="" component={Store}>
        <IndexRoute component={Landing}/>
        <Route path="about" component={About}/>
        <Route path="festivals" component={FestivalsContainer}/>
      </Route>
      <Route path="admin" component={Admin}/>
    </Route>
  </Router>


ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
