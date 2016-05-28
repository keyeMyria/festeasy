import React, { PropTypes } from 'react';
import AuthWrapper from './authWrapper.jsx'


export default class App extends React.Component {
  render() {
    return (
      <AuthWrapper>
        {this.props.children}
      </AuthWrapper>
    )
  }
}

App.propTypes = {
  children: PropTypes.object.isRequired,
}
