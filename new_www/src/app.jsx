import React, { PropTypes } from 'react';
import AuthWrapper from './authWrapper.jsx'
import StoreWrapper from './storeWrapper.jsx'


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
