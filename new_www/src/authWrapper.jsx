import React, { PropTypes } from 'react'
import axios from 'axios'


export default class AuthWrapper extends React.Component {
  constructor() {
    super()
    this.state = {
      isSigningIn: false,
      authSession: null,
      signInError: null,
    }
    this.signIn = this.signIn.bind(this)
    this.signOut = this.signOut.bind(this)
    this.onAuthSuccess = this.onAuthSuccess.bind(this)
    this.onAuthFailure = this.onAuthFailure.bind(this)
  }

  getChildContext() {
    const {
      authSession,
      isSigningIn,
      signInError,
    } = this.state
    return {
      authSession,
      isSigningIn,
      signInError,
      signIn: this.signIn,
      signOut: this.signOut,
    }
  }

  onAuthSuccess(session) {
    this.setState({
      isSigningIn: false,
      signInError: null,
      authSession: session,
    })
  }

  onAuthFailure(response) {
    localStorage.removeItem('authToken')
    this.setState({
      isSigningIn: false,
      signInError: {
        status: response.stats,
        statusText: response.statusText,
        data: response.data,
      },
    })
  }

  signIn(emailAddress, password) {
    axios({
      method: 'post',
      url: 'http://localhost:5000/api/v1/signin',
      data: {
        email_address: emailAddress,
        password,
      },
    })
    .then(response => {
      this.onAuthSuccess(response.data)
      this.context.router.push('/')
    })
    .catch(response => {
      this.onAuthFailure(response)
    })
  }

  signOut() {
    this.setState({
      isSigningIn: false,
      authSession: null,
      signInError: null,
    })
  }

  render() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
}

AuthWrapper.propTypes = {
  children: PropTypes.any,
}

AuthWrapper.contextTypes = {
  router: PropTypes.object.isRequired,
}

AuthWrapper.childContextTypes = {
  authSession: PropTypes.object,
  isSigningIn: PropTypes.bool,
  signIn: PropTypes.func,
  signOut: PropTypes.func,
  signInError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
}
