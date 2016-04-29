import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'

import Landing from './landing.jsx'


const App = React.createClass({
  render: function () {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
})


const About = React.createClass({
  render: function() {
    return (
      <div>
        <h1>About</h1>
      </div>
    )
  }
})


const Admin = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Admin</h1>
      </div>
    )
  }
})


const Store = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Store</h1>
        <Menu />
        {this.props.children}
      </div>
    )
  }
})


const MenuItem = React.createClass({
  render: function() {
    return (
        <Link className="item" to={this.props.to}>{this.props.text}</Link>
    )
  }
})


const Menu = React.createClass({
  render: function() {
    return (
      <div className="ui fixed menu">
        <div className="ui container">
          <div className="header item">
            <Link to="/">Home</Link>
          </div>
          <MenuItem to="/about" text="About" />
        </div>
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
      </Route>
      <Route path="admin" component={Admin}/>
    </Route>
  </Router>


ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
