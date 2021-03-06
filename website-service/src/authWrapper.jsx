import React, { PropTypes } from 'react'
import mixpanel from 'mixpanel-browser'
import axios from 'axios'


export default class AuthWrapper extends React.Component {
  static childContextTypes = {
    authDetails: PropTypes.object,
    signIn: PropTypes.func.isRequired,
    signUp: PropTypes.func.isRequired,
    signOut: PropTypes.func.isRequired,
    axios: PropTypes.func.isRequired,
  }

  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    children: PropTypes.any,
  }

  constructor() {
    super()
    let authDetails = null
    const sessionId = localStorage.getItem('sessionId')
    const sessionToken = localStorage.getItem('sessionToken')
    const userId = localStorage.getItem('userId')
    this.signIn = this.signIn.bind(this)
    this.signUp = this.signUp.bind(this)
    this.signOut = this.signOut.bind(this)
    this.persistAuthDetails = this.persistAuthDetails.bind(this)
    this.clearAuthDetails = this.clearAuthDetails.bind(this)
    this.requestInterceptor = this.requestInterceptor.bind(this)
    this.responseErrorInterceptor = this.responseErrorInterceptor.bind(this)
    axios.interceptors.request.use(this.requestInterceptor)
    axios.interceptors.response.use((r) => (r), this.responseErrorInterceptor)
    if (sessionId && sessionToken && userId) {
      authDetails = { sessionId, sessionToken, userId }
      mixpanel.identify(userId)
    } else {
      this.clearAuthDetails()
    }
    this.state = { authDetails, axios }
  }

  getChildContext() {
    const { authDetails } = this.state
    return {
      authDetails,
      axios,
      signIn: this.signIn,
      signUp: this.signUp,
      signOut: this.signOut,
    }
  }

  persistAuthDetails(sessionId, sessionToken, userId) {
    localStorage.setItem('sessionId', sessionId)
    localStorage.setItem('sessionToken', sessionToken)
    localStorage.setItem('userId', userId)
  }

  requestInterceptor(config) {
    const newConfig = Object.assign(config, {})
    if ('authDetails' in this.state && this.state.authDetails) {
      if ('sessionToken' in this.state.authDetails) {
        newConfig.headers.Authorization = this.state.authDetails.sessionToken
      }
    }
    return newConfig
  }

  responseErrorInterceptor(response) {
    const { router } = this.context
    if (response.status === 401) {
      this.setState({ authDetails: null })
      this.clearAuthDetails()
      router.push('/sign-in')
    }
    return Promise.reject(response)
  }

  clearAuthDetails() {
    localStorage.removeItem('sessionId')
    localStorage.removeItem('sessionToken')
    localStorage.removeItem('userId')
  }

  signUp(firstName, emailAddress, password) {
    return new Promise((resolve, reject) => {
      mixpanel.track('sign-up')
      axios({
        method: 'post',
        url: 'v1/auth/signup',
        data: { email_address: emailAddress, password, first_name: firstName },
      })
        .then(() => (
          this.signIn(emailAddress, password)
            .then((response) => {
              resolve(response)
            })
            .catch((error) => {
              reject(error)
            })
        ))
        .catch((error) => {
          reject(error)
        })
    })
  }

  signIn(emailAddress, password) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: 'v1/auth/signin',
        data: { email_address: emailAddress, password },
      })
        .then(response => {
          const session = response.data.session
          const user = response.data.user
          this.persistAuthDetails(session.id, session.token, session.user_id)
          mixpanel.identify(session.user_id)
          mixpanel.people.set({
            '$email': user.email_address,
            '$first_name': user.first_name,
          })
          mixpanel.track('sign-in')
          this.setState({
            authDetails: {
              sessionId: session.id,
              sessionToken: session.token,
              userId: session.user_id,
            },
          }, resolve(response))
        })
        .catch(response => {
          this.clearAuthDetails()
          reject(response)
        })
    })
  }

  signOut() {
    return new Promise((resolve) => {
      mixpanel.track('sign-out')
      this.setState({ authDetails: null })
      this.clearAuthDetails()
      this.context.router.push('/')
      resolve()
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
