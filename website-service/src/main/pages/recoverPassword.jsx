import React, { PropTypes } from 'react'
import { Input, Button, Form, Field, Message, Header } from 'semantic-react'
import AuthBox from 'main/components/authBox.jsx'


export default class RecoverPassword extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    axios: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
      emailAddress: '',
      isSubmitting: false,
      response: null,
      error: null,
    }
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  onSubmit(e) {
    e.preventDefault()
    const { axios } = this.context
    this.setState({ isSubmitting: true, error: null, response: null })
    const params = {
      'email_address': this.state.emailAddress,
    }
    axios({
      method: 'post',
      url: 'v1/auth/recover-password',
      data: params,
    })
      .then(() => {
        this.setState({
          isSubmitting: false,
          response: true,
          error: null,
        })
      })
      .catch((error) => {
        this.setState({
          isSubmitting: false,
          error: {
            body: error.data ? error.data.message : 'Something went wrong',
          },
        })
      })
  }

  onChange(e) {
    const state = {}
    state[e.target.name] = e.target.value
    this.setState(state)
  }

  render() {
    const { emailAddress, isSubmitting, response, error } = this.state
    let state = ''
    if (error) {
      state = 'error'
    } else if (response) {
      state = 'success'
    }
    return (
      <AuthBox title="Recover Password">
        <Form
          state={state}
          loading={!!isSubmitting}
          onSubmit={this.onSubmit}
        >
          <Message emphasis="error">
            <Header>Failed to send password reset email</Header>
            <p>{error ? error.body : 'Something went wrong'}</p>
          </Message>
          <Message emphasis="success">
            <Header>Successfully sent password reset email</Header>
            <p>Please check your email inbox</p>
          </Message>
          <Field required label="Email Address">
            <Input
              required
              type="text"
              name="emailAddress"
              onChange={this.onChange}
              value={emailAddress}
            />
          </Field>
          <Button type="submit">Submit</Button>
        </Form>
      </AuthBox>
    )
  }
}
