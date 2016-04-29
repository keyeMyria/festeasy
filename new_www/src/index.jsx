import '../semantic/dist/semantic.css'
import '../semantic/dist/semantic.js'

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'


const App = React.createClass({
  render: function () {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
})


const Landing = React.createClass({
  render: function () {
    return (
      <div>
        <h1 className="ui header">Landing here</h1>
        <button className="ui button">
          Follow
        </button>
        <Link to="/about">About</Link>
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


const routes =
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={Landing}/>
      <Route path="/about" component={About}/>
    </Route>
  </Router>

ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
