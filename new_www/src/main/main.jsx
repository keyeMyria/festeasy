import React, { PropTypes } from 'react';
import Navbar from './navbar.jsx'


export default class Main extends React.Component {
  render() {
    return (
      <div style={{ paddingTop: 55 }}>
        <Navbar />
        <div className="ui container">
          {this.props.children}
        </div>
      </div>
    )
  }
}

Main.propTypes = {
  children: PropTypes.object.isRequired,
}
