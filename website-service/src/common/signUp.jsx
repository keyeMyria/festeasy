import React, { PropTypes } from 'react'
import classNames from 'classnames'


export default class SignUp extends React.Component {
  static contextTypes = {
    signUp: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      emailAddress: '',
      password: '',
      isSigningUp: false,
      signUpError: null,
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSignUp = this.handleSignUp.bind(this)
  }

  handleChange(e) {
    const a = {}
    a[e.target.name] = e.target.value
    this.setState(a)
  }

  handleSignUp(e) {
    e.preventDefault()
    const { firstName, emailAddress, password } = this.state
    this.context.signUp(firstName, emailAddress, password)
  }

  render() {
    const {
      firstName,
      emailAddress,
      password,
      isSigningUp,
      signUpError,
    } = this.state
    const formClass = classNames({
      'ui form': true,
      'loading': isSigningUp,
      'error': signUpError !== null,
    })
    return (
      <div className="ui container centered grid">
        <div className="ui segment six wide column">
          <h1 className="ui header">Sign In</h1>
          <form className={formClass} onSubmit={this.handleSignUp}>
            <div className="ui error message">
              <div className="header">Failed to sign in</div>
              <p>Something went wrong</p>
            </div>
            <div className="ui field">
              <label>First Name</label>
              <input
                type="text"
                name="firstName"
                onChange={this.handleChange}
                value={firstName}
              />
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
            <button className="ui button" type="submit">Sign Up</button>
          </form>
        </div>
      </div>
    )
  }
}
