import React, { PropTypes } from 'react'
import classNames from 'classnames'


class SignIn extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      emailAddress: '',
      password: '',
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
    this.props.handleSignIn(emailAddress, password)
  }

  render() {
    const { emailAddress, password } = this.state
    const formClass = classNames({
      'ui form': true,
      'loading': this.props.isSigningIn,
      'error': this.props.signInError !== null,
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

SignIn.propTypes = {
  handleSignIn: PropTypes.func.isRequired,
  isSigningIn: PropTypes.bool.isRequired,
  signInError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
}


export default class SignInContainer extends React.Component {
  render() {
    return (
      <div>
        <SignIn
          isSigningIn={this.context.isSigningIn}
          signInError={this.context.signInError}
          handleSignIn={this.context.signIn}
        />
      </div>
    )
  }
}

SignInContainer.contextTypes = {
  signIn: PropTypes.func.isRequired,
  signInError: PropTypes.oneOfType([
    PropTypes.oneOf([null]),
    PropTypes.object,
  ]),
  isSigningIn: PropTypes.bool.isRequired,
}
