import React, { PropTypes } from 'react';
import axios from 'axios'
import NotificationSystem from 'react-notification-system'
import AuthWrapper from './authWrapper.jsx'
import StoreWrapper from './storeWrapper.jsx'
import apiEndpoint from './apiEndpoint.js'


axios.defaults.baseURL = apiEndpoint


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
