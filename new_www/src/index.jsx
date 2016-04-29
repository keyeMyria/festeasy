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
        <h1>Landing here</h1>
      </div>
    )
  }
})


const routes =
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={Landing}/>
    </Route>
  </Router>

ReactDOM.render(
  routes,
  document.getElementById('reactContent')
)
