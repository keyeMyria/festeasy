import React from 'react'
import MyInput from 'utils/myInput.jsx'
import MyButton from 'utils/myButton.jsx'
import MyForm from 'utils/myForm.jsx'
import AuthBox from 'main/components/authBox.jsx'


export default class RecoverPassword extends React.Component {
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
        <MyForm onSubmit={this.onSubmit}>
          <div className="ui error message">
            <div className="header">Failed to sign in</div>
            <p>Something went wrong</p>
          </div>
          <div className="ui field">
            <label htmlFor="emailAddress">Email Address</label>
            <MyInput
              type="text"
              name="emailAddress"
              onChange={this.onChange}
              value={emailAddress}
            />
          </div>
          <MyButton type="submit">Submit</MyButton>
        </MyForm>
      </AuthBox>
    )
  }
}
