// This module needs to be imported in the following way:
// import auth from './path/to/this/file' so that we can overrite
// onChange. Jesus.

import 'whatwg-fetch';


const parseJSON = function(response) {
  return response.json()
}


module.exports = {
  // TODO: Make less shit.
  signIn: function(email, password, cb) {
    const it = this
    cb = arguments[arguments.length -1]
    fetch('http://localhost:5000/api/v1/signin', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email_address: email,
        password: password
      })
    })
    .then(function(response) {
      if (response.status == 200) {
        return response
      } else {
        if (cb) cb(true)
        it.onChange(true)
        var error = new Error(response.statusText)
        error.response = response
        throw error
      }
    })
    .then(parseJSON)
    .then(function(json){
      if (cb) cb(true)
      localStorage.setItem('authToken', json.token)
      localStorage.setItem('authUserId', json.user_id)
      it.onChange(true)
    })
  },

  getAuthToken: function() {
    return localStorage.authToken
  },

  signOut: function(cb) {
    delete localStorage.authToken
    delete localStorage.authUserId
    if (cb) cb()
    this.onChange(false)
  },

  signedIn: function() {
    return !!(localStorage.authToken && localStorage.authUserId)
  },

  onChange: function() {}
}
