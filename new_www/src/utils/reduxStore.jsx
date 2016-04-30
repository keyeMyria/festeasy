import { createStore } from 'redux'

import appReducer from './reducers.jsx'


let store = createStore(appReducer)


module.exports = store
