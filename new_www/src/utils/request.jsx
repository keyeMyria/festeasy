import 'whatwg-fetch';
import getAuthDetails from './auth.jsx'


const fetchRequest = function(method, url, params, data, headers) {
  const settings = {
    method: method,
    headers: headers,
    body: data,
  }
  return fetch(url, settings)
}


const jsonApiRequest = function(method, url, params, data) {
  const baseUri = 'http://localhost:5000/api/v1'
  const authDetails = getAuthDetails()
  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
  if (authDetails) {
    headers.Authorization = authDetails.token
  }
  return fetchRequest(method, baseUri.concat(url), params, data, headers)
}


module.exports = {
  jsonApiRequest,
}
