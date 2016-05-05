/* eslint-disable */

import React from 'react';
import Formsy from 'formsy-react';
import auth from '../utils/auth.jsx'


const MyInput = React.createClass({
  mixins: [Formsy.Mixin],

  // setValue() will set the value of the component, which in
  // turn will validate it and the rest of the form
  changeValue(event) {
    this.setValue(event.currentTarget[this.props.type === 'checkbox' ? 'checked' : 'value']);
  },
  render() {

    // Set a specific className based on the validation
    // state of this component. showRequired() is true
    // when the value is empty and the required prop is
    // passed to the input. showError() is true when the
    // value typed is invalid
    const className = 'field' + (this.props.className || ' ') +
      (this.showRequired() ? 'required' : this.showError() ? 'error' : '');

    // An error message is returned ONLY if the component is invalid
    // or the server has returned an error message
    const errorMessage = this.getErrorMessage();

    return (
      <div className={className}>
        <label htmlFor={this.props.name}>{this.props.title}</label>
        <input
          type={this.props.type || 'text'}
          name={this.props.name}
          onChange={this.changeValue}
          value={this.getValue()}
          checked={this.props.type === 'checkbox' && this.getValue() ? 'checked' : null}
        />
      <div className='ui error message'>{errorMessage}</div>
      </div>
    );
  }
});


const SignInContainer = React.createClass({
  contextTypes: {
    router: React.PropTypes.object
  },

  contextTypes: {
    router: React.PropTypes.object,
  },

  getInitialState: function() {
    return { canSubmit: false }
  },

  submit: function(formData) {
    auth.signIn(formData.email_address, formData.password, (isSignedIn) => {
      if (isSignedIn) {
        this.context.router.push("/")
      } else {
        console.log('Error signing in.')
      }
    })
  },

  enableButton: function() {
    this.setState({ canSubmit: true })
  },

  disableButton: function() {
    this.setState({ canSubmit: false })
  },

  render: function() {
    return (
      <div>
        <h2>Sign In</h2>
        <Formsy.Form onSubmit={this.submit} onValid={this.enableButton} onInvalid={this.disableButton} className="ui form error">
          <MyInput name="email_address" title="Email" validations="isEmail" type="email" validationError="This is not a valid email" required />
          <MyInput name="password" title="Password" type="password" required />
          <button type="submit" className="ui button" disabled={!this.state.canSubmit}>Submit</button>
        </Formsy.Form>
      </div>
    );
  }
});


module.exports = SignInContainer
