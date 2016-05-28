import React, { PropTypes } from 'react'
import JSData from 'js-data'
import DSHttpAdapter from 'js-data-http'


export default class StoreWrapper extends React.Component {
  constructor() {
    super()
    this.state = {
      store: new JSData.DS(),
    }
    this.state.store.registerAdapter(
      'http',
      new DSHttpAdapter({ basePath: 'http://localhost:5000/api/v1' }),
      { default: true }
    )
    this.state.store.defineResource({
      name: 'product',
      endpoint: 'products',
    })
    this.state.store.defineResource({
      name: 'festival',
      endpoint: 'festivals',
    })
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
