import React from 'react'
import Lead from 'main/pages/landing/lead.jsx'
import Festivals from 'main/pages/landing/festivals.jsx'


export default class Landing extends React.Component {
  render() {
    return (
      <div style={{ marginTop: -15 }}>
        <Lead />
        <Festivals />
      </div>
    )
  }
}
