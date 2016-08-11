import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Form, Button, Input, Field } from 'semantic-react'
import AuthBox from 'main/components/authBox.jsx'


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
        let errorMessage = 'Something went wrong, please try again'
        if (error.status === 401) {
          errorMessage = 'Incorrent email address and password combination'
        }
        this.setState({
          isSigningIn: false,
          signInError: errorMessage,
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
        <Form
          state={signInError ? 'error' : ''}
          loading={!!isSigningIn}
          onSubmit={this.handleSignIn}
        >
          <div className="ui error message">
            <div className="header">Failed to sign in</div>
            <p>{signInError}</p>
          </div>
          <Field required label="Email Address">
            <Input
              required
              type="text"
              name="emailAddress"
              onChange={this.handleChange}
              value={emailAddress}
            />
          </Field>
          <Field required label="Password">
            <Input
              required
              type="password"
              name="password"
              onChange={this.handleChange}
              value={password}
            />
          </Field>
          <Button type="submit">Sign In</Button>
        </Form>
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
