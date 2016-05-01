import { combineReducers } from 'redux'
import { REQUEST_FETIVALS, RECEIVE_FESTVALS, requestFestivals, receiveFestivals } from './actions.jsx'


function festivals(state = {}, action) {
  switch (action.type) {
    case REQUEST_FETIVALS:
      return Object.assign({}, state, {
        isFetching: true,
        didInvalidate: false
      })
    case RECEIVE_FESTVALS:
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


const appReducer = combineReducers({
  festivals,
})


module.exports = appReducer
