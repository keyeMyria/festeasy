import React from 'react'
import mixpanel from 'mixpanel-browser'
import { Router, Route, browserHistory } from 'react-router'
import NotFound from 'common/pages/notFound.jsx'
import mainRoutes from 'main/routes.jsx'
import adminRoutes from 'admin/routes.jsx'
import App from 'app.jsx'


browserHistory.listen((e) => {
  mixpanel.track(
    'page-view',
    e,
  )
})


export default (
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      {adminRoutes}
      {mainRoutes}
    </Route>
    <Route path="*" component={NotFound} />
  </Router>
)
