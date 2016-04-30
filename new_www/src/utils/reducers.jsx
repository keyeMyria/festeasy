import { combineReducers } from 'redux'
import { SIGN_IN } from './actions.jsx'


function auth(state = {}, action) {
  switch (action.type) {
    case SIGN_IN:
      return {
          token: 'hah'
      }
    default:
      return state
  }
}


const appReducer = combineReducers({
  auth
})

module.exports = appReducer
