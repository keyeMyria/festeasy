import React from 'react';
import {
  Header,
} from 'semantic-react'
import voss from 'voss.jpg'


export default class Shop extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: `url('${voss}')`,
          backgroundSize: '100%',
          height: 600,
        }}
      >
        <Header
          style={{ color: 'white' }}
          aligned="center"
          size="large"
        >
          shop
        </Header>
      </div>
    )
  }
}
