import React, { PropTypes } from 'react'
import { Input, Button, Form, Field } from 'semantic-react'
import AuthBox from 'main/components/authBox.jsx'


export default class RecoverPassword extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      emailAddress: '',
    }
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  onSubmit(e) {
    e.preventDefault()
    const { store } = this.context
    store.create('forgotPasswordToken')
  }

  onChange(e) {
    const state = {}
    state[e.target.name] = e.target.value
    this.setState(state)
  }

  render() {
    const { emailAddress } = this.state
    return (
      <AuthBox title="Recover Password">
        <Form onSubmit={this.onSubmit}>
          <div className="ui error message">
            <div className="header">Failed to sign in</div>
            <p>Something went wrong</p>
          </div>
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
