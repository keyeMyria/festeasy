import React, { PropTypes } from 'react'
import axios from 'axios'


export default class AuthWrapper extends React.Component {
  constructor() {
    super()
    this.state = {
      isSigningUp: false,
      isSigningIn: false,
      isLoading: true,
      authSession: null,
      signInError: null,
      signUpError: null,
    }
    this.signUp = this.signUp.bind(this)
    this.signIn = this.signIn.bind(this)
    this.signOut = this.signOut.bind(this)
    this.onAuthSuccess = this.onAuthSuccess.bind(this)
    this.onAuthFailure = this.onAuthFailure.bind(this)
  }

  getChildContext() {
    const {
      authSession,
      isSigningIn,
      isSigningUp,
      signInError,
      signUpError,
    } = this.state
    return {
      authSession,
      isSigningIn,
      isSigningUp,
      signInError,
      signUpError,
      signUp: this.signUp,
      signIn: this.signIn,
      signOut: this.signOut,
    }
  }

  componentWillMount() {
    const sessionId = localStorage.getItem('authSessionId')
    const sessionToken = localStorage.getItem('authSessionToken')
    if (sessionId && sessionToken) {
      axios({
        method: 'get',
        url: `v1/sessions/${sessionId}`,
        headers: {
          Authorization: sessionToken,
        },
      })
      .then((response) => {
        this.onAuthSuccess(response.data)
        this.setState({ isLoading: false })
      })
      .catch(() => {
        localStorage.removeItem('authSessionId')
        localStorage.removeItem('authSessionToken')
        this.setState({ isLoading: false })
      })
    } else {
      localStorage.removeItem('authSessionId')
      localStorage.removeItem('authSessionToken')
      this.setState({ isLoading: false })
    }
  }

  onAuthSuccess(session) {
    localStorage.setItem('authSessionId', session.id)
    localStorage.setItem('authSessionToken', session.token)
    this.setState({
      isSigningIn: false,
      signInError: null,
      authSession: session,
    })
  }

  onAuthFailure(response) {
    localStorage.removeItem('authSessionId')
    localStorage.removeItem('authSessionToken')
    this.setState({
      isSigningIn: false,
      authSession: null,
      signInError: {
        status: response.stats,
        statusText: response.statusText,
        data: response.data,
      },
    })
  }

  signUp(firstName, emailAddress, password) {
    this.setState({ isSigningUp: true })
    axios({
      method: 'post',
      url: 'v1/signup',
      data: {
        first_name: firstName,
        email_address: emailAddress,
        password,
      },
    })
    .then(() => {
      this.signIn(emailAddress, password)
      this.setState({
        signUpError: null,
        isSigningUp: false,
      })
    })
    .catch(response => {
      this.setState({
        signUpError: response,
        isSigningUp: false,
      })
    })
  }

  signIn(emailAddress, password) {
    this.setState({ isSigningIn: true })
    axios({
      method: 'post',
      url: 'v1/signin',
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
    localStorage.removeItem('authSessionId')
    localStorage.removeItem('authSessionToken')
    this.setState({
      isSigningIn: false,
      authSession: null,
      signInError: null,
    })
  }

  render() {
    const { isLoading } = this.state
    if (isLoading) {
      return (
        <div className="ui active centered large inline loader"></div>
      )
    } else {
      return (
        <div>
          {this.props.children}
        </div>
      )
    }
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
  isSigningUp: PropTypes.bool,
  signUp: PropTypes.func,
  signIn: PropTypes.func,
  signOut: PropTypes.func,
  signUpError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
  signInError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
}
