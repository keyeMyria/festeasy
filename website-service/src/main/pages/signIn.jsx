import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import AuthBox from 'main/components/authBox.jsx'
import { MyForm, MyButton, MyInput } from 'utils/index.jsx'


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
    const { router } = this.context
    const { emailAddress, password } = this.state
    this.setState({ isSigningIn: true })
    this.context.signIn(emailAddress, password)
      .then(() => {
        router.push('/store')
      })
      .catch((error) => {
        console.log(error)
        this.setState({
          isSigningIn: false,
          signInError: error.data ? error.data.message : 'Something went wrong, please try again',
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
    return (
      <AuthBox title="Sign In">
        <MyForm
          state={signInError ? 'error' : ''}
          loading={!!isSigningIn}
          onSubmit={this.handleSignIn}
        >
          <div className="ui error message">
            <div className="header">Failed to sign in</div>
            <p>{signInError}</p>
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
          <MyButton type="submit">Sign In</MyButton>
        </MyForm>
        <div>
          Dont have an account yet? <Link to="/sign-up">Sign up</Link>
        </div>
        <div>
          Forgot your password? <Link to="recover-password">Recover password</Link>
        </div>
      </AuthBox>
    )
  }
}
