import React from 'react'
import { Router, Route, browserHistory } from 'react-router'
import NotFound from 'common/pages/notFound.jsx'
import mainRoutes from 'main/routes.jsx'
import App from 'app.jsx'


export default (
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      {mainRoutes}
    </Route>
    <Route path="*" component={NotFound} />
  </Router>
)
