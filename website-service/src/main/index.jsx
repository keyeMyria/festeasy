import React, { PropTypes } from 'react';
import Navbar from 'main/components/navbar.jsx'
import CartContainer from 'main/pages/cartContainer.jsx'
import CartPanel from './cartPanel.jsx'


export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }


  render() {
    return (
      <div style={{ paddingTop: 55 }}>
        <Navbar />
        <CartContainer>
          <CartPanel />
        </CartContainer>
        <div className="ui container">
          {this.props.children}
        </div>
      </div>
    )
  }
}
