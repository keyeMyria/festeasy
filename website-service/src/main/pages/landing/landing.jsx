import React from 'react'
import Lead from 'main/pages/landing/lead.jsx'
import Festivals from 'main/pages/landing/festivals.jsx'
import Shop from 'main/pages/landing/shop.jsx'


export default class Landing extends React.Component {
  render() {
    return (
      <div>
        <Lead />
        <Festivals />
        <Shop />
      </div>
    )
  }
}
