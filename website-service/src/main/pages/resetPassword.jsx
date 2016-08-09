import React, { PropTypes } from 'react'
import { Message, Header, Form, Field, Button, Input } from 'semantic-react'
import AuthBox from 'main/components/authBox.jsx'


export default class ResetPassword extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      isLoading: true,
      fpt: null,
      fptError: null,
      newPassword: '',
      newPasswordConfirmation: '',
      isSubmitting: false,
      changePasswordResult: null,
      changePasswordError: null,
    }
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  componentDidMount() {
    const { store } = this.context
    const params = {
      token: this.props.location.query.token,
    }
    store.findAll('forgotPasswordToken', params)
      .then((fpts) => {
        const state = {}
        state.isLoading = false
        if (fpts.length === 0) {
          state.fptError = 'Token not found'
        } else if (fpts.length === 1) {
          state.fpt = fpts[0]
        } else {
          state.fptError = 'Something went wrong'
        }
        this.setState(state)
      })
      .catch(() => {
        this.setState({
          fptError: 'Failed to find token',
        })
      })
  }

  onSubmit(e) {
    e.preventDefault()
    const { axios } = this.context
    const { newPassword, newPasswordConfirmation, fpt } = this.state
    if (newPassword !== newPasswordConfirmation) {
      this.setState({
        changePasswordError: 'Passwords do not match',
      })
      return
    }
    this.setState({ changePasswordError: null, isSubmitting: true })
    axios({
      method: 'post',
      url: 'v1/auth/reset-password',
      data: {
        token: fpt.token,
        password: newPassword,
      },
    })
      .then(() => {
        this.setState({
          isSubmitting: false,
          changePasswordError: null,
          changePasswordResult: true,
        })
      })
      .catch(() => {
        this.setState({
          isSubmitting: false,
          changePasswordError: 'Something went wrong',
        })
      })
  }

  onChange(e) {
    const state = {}
    state[e.target.name] = e.target.value
    this.setState(state)
  }

  getForm() {
    const {
      newPassword,
      newPasswordConfirmation,
      changePasswordResult,
      changePasswordError,
      isSubmitting,
    } = this.state
    let state = ''
    if (changePasswordError) {
      state = 'error'
    } else if (changePasswordResult) {
      state = 'success'
    }
    return (
      <Form
        state={state}
        loading={!!isSubmitting}
        onSubmit={this.onSubmit}
      >
        <Message emphasis="error">
          <Header>Failed to reset password</Header>
          <p>{changePasswordError}</p>
        </Message>
        <Message emphasis="success">
          <Header>Successfully reset password</Header>
        </Message>
        <Field required label="New Password">
          <Input
            required
            type="password"
            name="newPassword"
            onChange={this.onChange}
            value={newPassword}
          />
        </Field>
        <Field required label="Confirm New Password">
          <Input
            required
            type="password"
            name="newPasswordConfirmation"
            onChange={this.onChange}
            value={newPasswordConfirmation}
          />
        </Field>
        <Button type="submit">Submit</Button>
      </Form>
    )
  }

  render() {
    const { fpt, fptError } = this.state
    let result = <div>Loading...</div>
    if (fptError) {
      result = <Message emphasis="warning">{fptError}</Message>
    } else if (fpt) {
      result = this.getForm()
    }
    return (
      <AuthBox title="Reset Password">
        {result}
      </AuthBox>
    )
  }
}
