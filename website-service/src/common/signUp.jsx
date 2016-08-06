import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import classNames from 'classnames'


export default class SignUp extends React.Component {
  static contextTypes = {
    signUp: PropTypes.func.isRequired,
    router: PropTypes.object.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
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
    const { router } = this.context
    const { firstName, emailAddress, password } = this.state
    this.setState({ isSigningUp: true })
    this.context.signUp(firstName, emailAddress, password)
      .then(() => {
        router.push('/store')
      })
      .catch((error) => {
        this.setState({
          isSigningUp: false,
          signUpError: error.data ? error.data.message : 'Something went wrong, please try again',
        })
      })
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
          <h1 className="ui header">Sign Up</h1>
          <form className={formClass} onSubmit={this.handleSignUp}>
            <div className="ui error message">
              <div className="header">Failed to sign up</div>
              <p>{signUpError}</p>
            </div>
            <div className="ui field">
              <label htmlFor="firstName">First Name</label>
              <input
                type="text"
                name="firstName"
                onChange={this.handleChange}
                value={firstName}
              />
            </div>
            <div className="ui field">
              <label htmlFor="emailAddress">Email Address</label>
              <input
                type="text"
                name="emailAddress"
                onChange={this.handleChange}
                value={emailAddress}
              />
            </div>
            <div className="ui field">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                name="password"
                onChange={this.handleChange}
                value={password}
              />
            </div>
            <button className="ui button" type="submit">Sign Up</button>
          </form>
          Already have an account? <Link to="/sign-in">Sign in</Link>
        </div>
      </div>
    )
  }
}
