import { SIGN_IN } from './actions.jsx'


const signIn = function signIn(emailAddress, password) {
  return {
    type: SIGN_IN,
    emailAddress: emailAddress,
    password: password
  }
}


const fetchFestivals =  (festivals) => ({
  type: FETCH_FESTIVALS,
  festivals: festivals,
})


module.exports = {
  signIn,
}
