import React, { PropTypes } from 'react'
import { Header, Form, Field, Input, Button } from 'semantic-react'


class ChangePassword extends React.Component {
  static contextTypes = {
    authDetails: PropTypes.object.isRequired,
    addNotification: PropTypes.func.isRequired,
    axios: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
      currentPassword: '',
      newPassword: '',
      status: '',
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    const a = {}
    a[e.target.name] = e.target.value
    this.setState(a)
  }

  handleSubmit(e) {
    e.preventDefault()
    const { addNotification, axios, authDetails } = this.context
    const { currentPassword, newPassword } = this.state
    axios({
      method: 'post',
      url: `v1/users/${authDetails.userId}/change-password`,
      data: {
        'current_password': currentPassword,
        'new_password': newPassword,
      },
    })
      .then(() => {
        addNotification({
          message: 'Successfully changed password.',
          level: 'success',
        })
      })
      .catch(() => {
        addNotification({
          message: 'Failed to change password.',
          level: 'error',
        })
      })
  }

  render() {
    const { currentPassword, newPassword } = this.state
    return (
      <div>
        <Header>Change Password</Header>
        <Form onSubmit={this.handleSubmit}>
          <Field label="Current Password">
            <Input
              name="currentPassword"
              type="password"
              onChange={this.handleChange}
              value={currentPassword}
            />
          </Field>
          <Field label="New Password">
            <Input
              name="newPassword"
              type="password"
              onChange={this.handleChange}
              value={newPassword}
            />
          </Field>
          <Button>Change Password</Button>
        </Form>
      </div>
    )
  }
}


export default class Settings extends React.Component {
  render() {
    return (
      <div>
        <Header>Settings</Header>
        <ChangePassword />
      </div>
    )
  }
}
