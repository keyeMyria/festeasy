import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import { Form, Input, Button, Field } from 'semantic-react'
import AuthBox from 'main/components/authBox.jsx'


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
        let errorMessage = 'Something went wrong, please try again'
        if (error.status === 409) {
          errorMessage = 'Account already exists'
        }
        this.setState({
          isSigningUp: false,
          signUpError: errorMessage,
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
        <Form
          state={signUpError ? 'error' : ''}
          loading={!!isSigningUp}
          onSubmit={this.handleSignUp}
        >
          <div className="ui error message">
            <div className="header">Failed to sign up</div>
            <p>{signUpError}</p>
          </div>
          <Field required label="First Name">
            <Input
              required
              type="text"
              name="firstName"
              onChange={this.handleChange}
              value={firstName}
            />
          </Field>
          <Field required label="Email Address">
            <Input
              required
              type="text"
              name="emailAddress"
              onChange={this.handleChange}
              value={emailAddress}
            />
          </Field>
          <Field required label="Pasword">
            <Input
              required
              type="password"
              name="password"
              onChange={this.handleChange}
              value={password}
            />
          </Field>
          <Button type="submit">Sign Up</Button>
        </Form>
        <div>
          Already have an account? <Link to="/sign-in">Sign in</Link>
        </div>
        <div>
          Forgot your password? <Link to="recover-password">Recover password</Link>
        </div>
      </AuthBox>
    )
  }
}
