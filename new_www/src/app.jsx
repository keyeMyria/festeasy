import React, { PropTypes } from 'react';
import axios from 'axios'
import AuthWrapper from './authWrapper.jsx'
import StoreWrapper from './storeWrapper.jsx'
import apiEndpoint from './apiEndpoint.js'


axios.defaults.baseURL = apiEndpoint


export default class App extends React.Component {
  render() {
    return (
      <AuthWrapper>
        <StoreWrapper>
          {this.props.children}
        </StoreWrapper>
      </AuthWrapper>
    )
  }
}

App.propTypes = {
  children: PropTypes.object.isRequired,
}
