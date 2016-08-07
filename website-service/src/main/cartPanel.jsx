import React, { PropTypes } from 'react';
import { Motion, spring } from 'react-motion';

// import { MenuItem } from 'semantic-react'
// import { Tab } from 'semantic-react'
// import Tabs from '../components/sidePanel/tabs.jsx'
// import TabMenu from '../components/sidePanel/tabmenu.jsx'
// import Tab from '../components/sidePanel/tab.jsx'

// import CartItem from './cartItem.jsx'
const styler = {
  position: 'absolute',
  borderRadius: '1%',
  paddingTop: '60px',
  overflowX: 'hidden',
  WebkitBoxSizing: 'border-box', /* Safari/Chrome, other WebKit */
  // -moz-box-sizing: border-box,    /* Firefox, other Gecko */
  // box-sizing: border-box,
  boxSizing: 'border-box',
  paddingLeft: 20,
  backgroundColor: '#68AEF0',
  cursor: 'pointer',
  justifyContent: 'center',
}

export default class CartPanel extends React.Component {
  static propTypes = {
    children: PropTypes.any,
  }
  constructor(props) {
    super(props);
    this.state = {
      active: 2,
      open: false,
    }
    this.initialStyle = this.initialStyle.bind(this)
    this.finalStyle = this.finalStyle.bind(this)
    this.close = this.close.bind(this)
  }
  initialStyle() {
    return {
      width: spring(19, { stiffness: 120, damping: 20 }),
      height: spring('90%', { stiffness: 100, damping: 10 }),
      right: spring(0, { stiffness: 100, damping: 10 }),
    }
  }
  finalStyle() {
    return {
      width: spring(400, { stiffness: 120, damping: 26 }),
      height: spring(400, { stiffness: 100, damping: 10 }),
      right: spring(0, { stiffness: 100, damping: 10 }),
    }
  }
  close() {
    const { open } = this.state
    this.setState({
      open: !open,
    })
  }

  render() {
    const { open } = this.state
    const style = !open ? this.initialStyle() : this.finalStyle()
    return (
      <Motion style={style}>
        {({ width, height, right }) => (
          <div
            style={{
              ...styler,
              width: width,
              height: height,
              right: right,
            }} onClick={() => this.close()}
          >
          {this.props.children}
          </div>
        )
        }
      </Motion>
    )
  }
}
