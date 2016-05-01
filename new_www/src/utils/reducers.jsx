import { combineReducers } from 'redux'
import { REQUEST_FETIVALS, RECEIVE_FESTVALS_SUCCESS, } from './actions.jsx'


function festivals(state = {}, action) {
  switch (action.type) {
    case REQUEST_FETIVALS:
      return Object.assign({}, state, {
        isFetching: true,
        didInvalidate: false
      })
    case RECEIVE_FESTVALS_SUCCESS:
      return Object.assign({}, state, {
        isFetching: false,
        didInvalidate: false,
        items: action.festivals,
        recievedOn: action.recievedOn
      })
    default:
      return state
  }
}


const rootReducer = combineReducers({
  festivals,
})


module.exports = rootReducer
