import React, { PropTypes } from 'react'
import axios from 'axios'


export default class AuthWrapper extends React.Component {
  constructor() {
    super()
    this.state = {
      isSigningIn: false,
      isLoading: false,
      authSession: null,
      authUser: null,
      signInError: null,
    }
    this.signIn = this.signIn.bind(this)
    this.signOut = this.signOut.bind(this)
    this.getAuthUser = this.getAuthUser.bind(this)
    this.onAuthSuccess = this.onAuthSuccess.bind(this)
    this.onAuthFailure = this.onAuthFailure.bind(this)
  }

  getChildContext() {
    const {
      authSession,
      authUser,
      isSigningIn,
      signInError,
    } = this.state
    return {
      authSession,
      authUser,
      isSigningIn,
      signInError,
      signIn: this.signIn,
      signOut: this.signOut,
    }
  }

  componentWillMount() {
    const sessionId = localStorage.getItem('authSessionId')
    const sessionToken = localStorage.getItem('authSessionToken')
    if (sessionId && sessionToken) {
      this.setState({ isLoading: true })
      axios({
        method: 'get',
        url: `v1/sessions/${sessionId}`,
        headers: {
          Authorization: sessionToken,
        },
      })
      .then((response) => {
        this.setState({ isLoading: false })
        this.onAuthSuccess(response.data)
      })
      .catch(() => {
        this.setState({ isLoading: false })
        localStorage.removeItem('authSessionId')
        localStorage.removeItem('authSessionToken')
      })
    } else {
      localStorage.removeItem('authSessionId')
      localStorage.removeItem('authSessionToken')
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
    this.getAuthUser(session)
  }

  onAuthFailure(response) {
    localStorage.removeItem('authSessionId')
    localStorage.removeItem('authSessionToken')
    this.setState({
      isSigningIn: false,
      authSession: null,
      authUser: null,
      signInError: {
        status: response.stats,
        statusText: response.statusText,
        data: response.data,
      },
    })
  }

  getAuthUser(session) {
    axios({
      method: 'get',
      url: `v1/users/${session.user_id}`,
      headers: {
        Authorization: session.token,
      },
    })
    .then((response) => {
      this.setState({
        authUser: response.data,
      })
    })
  }

  signIn(emailAddress, password) {
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
      authUser: null,
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
  authUser: PropTypes.object,
  isSigningIn: PropTypes.bool,
  signIn: PropTypes.func,
  signOut: PropTypes.func,
  signInError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
}
