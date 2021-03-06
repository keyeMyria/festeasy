/* eslint react/no-string-refs: "off" */

import React, { PropTypes } from 'react';
import axios from 'axios'
import mixpanel from 'mixpanel-browser'
import NotificationSystem from 'react-notification-system'
import AuthWrapper from 'authWrapper.jsx'
import StoreWrapper from 'storeWrapper.jsx'
import apiEndpoint from 'apiEndpoint.js'
import mixpanelToken from 'mixpanelToken.js'


axios.defaults.baseURL = apiEndpoint
mixpanel.init(mixpanelToken)


export default class App extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }

  static childContextTypes = {
    addNotification: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.addNotification = this.addNotification.bind(this)
  }

  getChildContext() {
    return {
      addNotification: this.addNotification,
    }
  }

  addNotification(notificaton) {
    this.refs.notificationSystem.addNotification(notificaton)
  }

  render() {
    return (
      <AuthWrapper>
        <StoreWrapper>
          <NotificationSystem ref="notificationSystem" />
          {this.props.children}
        </StoreWrapper>
      </AuthWrapper>
    )
  }
}
