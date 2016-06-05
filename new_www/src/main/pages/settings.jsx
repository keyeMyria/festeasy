import React from 'react'


class ChangePassword extends React.Component {
  render() {
    return (
      <div className="ui segment">
        <h3 className="ui header">Change Password</h3>
        <form className="ui form">
          <div className="field">
            <label>Current password</label>
            <input type="password" />
          </div>
          <div className="field">
            <label>New password</label>
            <input type="password" />
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
