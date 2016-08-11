import React, { PropTypes } from 'react'
import { Header, Divider } from 'semantic-react'


export default class Festivals extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  render() {
    return (
      <div>
        <Header aligned="center">Festivals</Header>
        <Divider />
        {this.props.children}
      </div>
    )
  }
}
