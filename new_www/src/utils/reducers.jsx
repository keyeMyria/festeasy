import { combineReducers } from 'redux'
import { SIGN_IN, FETCH_FESTIVALS } from './actions.jsx'


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


function festivals(state = [], action) {
  switch (action.type) {
    case FETCH_FESTIVALS:
      return action.festivals
    default:
      return state
  }
}


const appReducer = combineReducers({
  auth,
  festivals
})


module.exports = appReducer
