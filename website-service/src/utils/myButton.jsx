import React from 'react'
import { Button } from 'semantic-react'


export default class MyButton extends React.Component {
  render() {
    return (
      <Button {...this.props} />
    )
  }
}
