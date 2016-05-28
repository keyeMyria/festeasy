import React, { PropTypes } from 'react'
import JSData from 'js-data'
import DSHttpAdapter from 'js-data-http'
import models from './models.js'


export default class StoreWrapper extends React.Component {
  constructor() {
    super()
    const store = new JSData.DS()
    store.registerAdapter(
      'http',
      new DSHttpAdapter({ basePath: 'http://localhost:5000/api/v1' }),
      { default: true }
    )
    models.forEach((model) => {
      store.defineResource(model)
    })
    this.state = {
      store,
    }
  }

  getChildContext() {
    return {
      store: this.state.store,
    }
  }

  render() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
}

StoreWrapper.propTypes = {
  children: PropTypes.any.isRequired,
}

StoreWrapper.childContextTypes = {
  store: PropTypes.object.isRequired,
}
