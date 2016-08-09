import React, { PropTypes } from 'react'


class ChangePassword extends React.Component {
  static contextTypes = {
    authDetails: PropTypes.object.isRequired,
    addNotification: PropTypes.func.isRequired,
    axios: PropTypes.object.isRequired,
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
      <div className="ui segment">
        <h3 className="ui header">Change Password</h3>
        <form className="ui form" onSubmit={this.handleSubmit}>
          <div className="field">
            <label htmlFor="currentPassword">Current password</label>
            <input
              name="currentPassword"
              type="password"
              onChange={this.handleChange}
              value={currentPassword}
            />
          </div>
          <div className="field">
            <label htmlFor="newPassword">New password</label>
            <input
              name="newPassword"
              type="password"
              onChange={this.handleChange}
              value={newPassword}
            />
          </div>
          <button className="ui button">Change Password</button>
        </form>
      </div>
    )
  }
}


export default class Settings extends React.Component {
  render() {
    return (
      <div>
        <h1 className="ui header">Settings</h1>
        <ChangePassword />
      </div>
    )
  }
}
