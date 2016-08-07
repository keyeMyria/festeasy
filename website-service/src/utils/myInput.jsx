import React from 'react'
import { Input } from 'semantic-react'


export default class MyInput extends React.Component {
  render() {
    return (
      <Input
        {...this.props}
      />
    )
  }
}
