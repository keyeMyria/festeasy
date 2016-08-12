import React, { PropTypes } from 'react';
import Navbar from 'main/components/navbar.jsx'


export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }

  render() {
    return (
      <div>
        <Navbar />
        <div className="ui container">
          {this.props.children}
        </div>
      </div>
    )
  }
}
