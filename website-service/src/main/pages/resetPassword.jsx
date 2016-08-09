import React, { PropTypes } from 'react'
import AuthBox from 'main/components/authBox.jsx'


export default class ResetPassword extends React.Component {
  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      newPassword: '',
      newPasswordConfirmation: '',
    }
  }

  render() {
    return (
      <AuthBox title="Reset Password">
        Hi
      </AuthBox>
    )
  }
}
