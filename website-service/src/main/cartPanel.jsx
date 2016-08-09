import React, { PropTypes } from 'react';
import ReactDOM from 'react-dom';
import { Motion, spring } from 'react-motion';

// import { MenuItem } from 'semantic-react'
// import { Tab } from 'semantic-react'
// import Tabs from '../components/sidePanel/tabs.jsx'
// import TabMenu from '../components/sidePanel/tabmenu.jsx'
// import Tab from '../components/sidePanel/tab.jsx'

// import CartItem from './cartItem.jsx'
const styler = {
  position: 'absolute',
  zIndex: 5,
  paddingTop: '60px',
  borderRadius: '0.5%',
  overflowX: 'hidden',
  WebkitBoxSizing: 'border-box', /* Safari/Chrome, other WebKit */
  // -moz-box-sizing: border-box,    /* Firefox, other Gecko */
  // box-sizing: border-box,
  boxSizing: 'border-box',
  backgroundColor: 'white',
  // borderColor: '#2A8EFF',
  // borderStyle: 'solid',
  // borderSize: '0.3em',
  cursor: 'pointer',
  boxShadow: '-5px 2px 5px #afafaf',
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
    this.dimDoc = this.dimDoc.bind(this)
    this.handleClick = this.handleClick.bind(this)
  }
  componentWillMount() {
    document.addEventListener('click', this.handleClick, false)
  }
  componentDidMount() {
    this.setState({
      open: true,
    })
  }
  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }
  initialStyle() {
    return {
      width: spring(0, { stiffness: 150, damping: 20 }),
      height: spring(10, { stiffness: 100, damping: 20 }),
      right: spring(0, { stiffness: 100, damping: 10 }),
    }
  }
  handleClick(e) {
    if (!ReactDOM.findDOMNode(this).contains(e.target) && this.state.open) {
      const { open } = this.state
      this.setState({
        open: !open,
      })
    }
  }
  finalStyle() {
    return {
      width: spring(700, { stiffness: 150, damping: 26 }),
      height: spring(600, { stiffness: 100, damping: 20 }),
      right: spring(0, { stiffness: 100, damping: 10 }),
    }
  }
  dimDoc() {
    const opac = 0.2
    document.body.style.backgroundColor = `rgba(0,0,0,${opac})`
  }
  undimDoc() {
    const opac = 0
    document.body.style.backgroundColor = `rgba(0,0,0,${opac})`
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
    // open ? this.dimDoc() : this.undimDoc()
    return (
      <Motion style={style} >
        {({ width, height, right }) => (
          <div
            style={{
              ...styler,
              width: width,
              height: height,
              right: right,
            }}
          >
            {open ? this.props.children : null}
          </div>
        )
        }
      </Motion>
    )
  }
}
