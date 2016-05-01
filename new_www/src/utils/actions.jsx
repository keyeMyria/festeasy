import { jsonApiRequest } from './request.jsx'


const REQUEST_FETIVALS = 'REQUEST_FETIVALS'
const RECEIVE_FESTVALS_SUCCESS = 'FETCH_FESTIVALS_SUCCESS'


const requestFestivals = function() {
  return {
    type: REQUEST_FETIVALS
  }
}


const receiveFestivalsSuccess = function(json) {
  return {
    type: RECEIVE_FESTVALS_SUCCESS,
    items: json,
    recievedOn: Date.now()
  }
}


const fetchFestivals = function() {
  return function(dispatch){
    dispatch(requestFestivals())
    return jsonApiRequest('get', '/festivals')
      .then(response => response.json())
      .then(json =>
        dispatch(receiveFestivalsSuccess(json))
      )
  }
}


module.exports = {
  REQUEST_FETIVALS,
  RECEIVE_FESTVALS_SUCCESS,
  requestFestivals,
  receiveFestivalsSuccess,
  fetchFestivals
}
