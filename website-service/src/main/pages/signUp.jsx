import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import AuthBox from 'main/components/authBox.jsx'
import { MyForm, MyInput, MyButton } from 'utils/index.jsx'


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
    return (
      <AuthBox title="Sign Up">
        <MyForm
          state={signUpError ? 'error' : ''}
          loading={!!isSigningUp}
          onSubmit={this.handleSignUp}
        >
          <div className="ui error message">
            <div className="header">Failed to sign up</div>
            <p>{signUpError}</p>
          </div>
          <div className="ui field">
            <label htmlFor="firstName">First Name</label>
            <MyInput
              type="text"
              name="firstName"
              onChange={this.handleChange}
              value={firstName}
            />
          </div>
          <div className="ui field">
            <label htmlFor="emailAddress">Email Address</label>
            <MyInput
              type="text"
              name="emailAddress"
              onChange={this.handleChange}
              value={emailAddress}
            />
          </div>
          <div className="ui field">
            <label htmlFor="password">Password</label>
            <MyInput
              type="password"
              name="password"
              onChange={this.handleChange}
              value={password}
            />
          </div>
          <MyButton type="submit">Sign Up</MyButton>
        </MyForm>
        <div>
          Already have an account? <Link to="/sign-in">Sign in</Link>
        </div>
      </AuthBox>
    )
  }
}
