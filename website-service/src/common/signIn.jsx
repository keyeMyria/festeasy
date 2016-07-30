import React, { PropTypes } from 'react'
import classNames from 'classnames'


export default class SignIn extends React.Component {
  static contextTypes = {
    signIn: PropTypes.func.isRequired,
    router: PropTypes.object.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      emailAddress: '',
      password: '',
      isSigningIn: false,
      signInError: null,
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSignIn = this.handleSignIn.bind(this)
  }

  handleChange(e) {
    const a = {}
    a[e.target.name] = e.target.value
    this.setState(a)
  }

  handleSignIn(e) {
    e.preventDefault()
    const { emailAddress, password } = this.state
    this.context.signIn(emailAddress, password)
      .then(() => {
        this.setState({
          isSigningIn: false,
        })
      })
      .catch((error) => {
        this.setState({
          isSigningIn: false,
          signInError: error.data ? error.data.message : 'Something went wrong',
        })
      })
  }

  render() {
    const {
      emailAddress,
      password,
      isSigningIn,
      signInError,
    } = this.state
    const formClass = classNames({
      'ui form': true,
      'loading': isSigningIn,
      'error': signInError !== null,
    })
    return (
      <div className="ui container centered grid">
        <div className="ui segment six wide column">
          <h1 className="ui header">Sign In</h1>
          <form className={formClass} onSubmit={this.handleSignIn}>
            <div className="ui error message">
              <div className="header">Failed to sign in</div>
              <p>Something went wrong</p>
            </div>
            <div className="ui field">
              <label>Email Address</label>
              <input
                type="text"
                name="emailAddress"
                onChange={this.handleChange}
                value={emailAddress}
              />
            </div>
            <div className="ui field">
              <label>Password</label>
              <input
                type="password"
                name="password"
                onChange={this.handleChange}
                value={password}
              />
            </div>
            <button className="ui button" type="submit">Sign In</button>
          </form>
        </div>
      </div>
    )
  }
}
