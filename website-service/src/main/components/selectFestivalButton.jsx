import React, { PropTypes } from 'react'
import { Button } from 'semantic-react'


export default class SelectFestivalButton extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
    router: PropTypes.object.isRequired,
    authDetails: PropTypes.object,
  }

  static propTypes = {
    festival: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.onClick = this.onClick.bind(this)
  }

  onClick() {
    const { authDetails, router, store } = this.context
    const { festival } = this.props
    if (authDetails) {
      store.find('user', authDetails.userId, { bypassCache: true })
      .then((user) => {
        store.update(
          'cart',
          user.cart_id,
          { 'festival_id': festival.id },
          { method: 'patch' }
        )
      })
    }
    router.push('/store')
  }

  render() {
    return (
      <Button
        color="green"
        onClick={this.onClick}
      >
        Select
      </Button>
    )
  }
}
