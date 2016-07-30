import React, { PropTypes } from 'react'
import JSData from 'js-data'
import DSHttpAdapter from 'js-data-http'
import models from './models.js'


export default class StoreWrapper extends React.Component {
  static childContextTypes = {
    store: PropTypes.object.isRequired,
  }

  static contextTypes = {
    authDetails: PropTypes.object,
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  constructor(props, context) {
    super(props)
    const store = new JSData.DS()
    store.registerAdapter(
        'http',
        new DSHttpAdapter({
          http: context.axios,
        }),
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
