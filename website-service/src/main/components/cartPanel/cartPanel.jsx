import React, { PropTypes } from 'react';
import { Motion, spring } from 'react-motion';
import CartItem from './cartItem.jsx'

// import { MenuItem } from 'semantic-react'
// import { Tab } from 'semantic-react'
// import Tabs from '../components/sidePanel/tabs.jsx'
// import TabMenu from '../components/sidePanel/tabmenu.jsx'
// import Tab from '../components/sidePanel/tab.jsx'

// import CartItem from './cartItem.jsx'
const styler = {
  position: 'fixed',
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
  // borderSize: '0em',
  cursor: 'pointer',
  boxShadow: '-5px 2px 5px #afafaf',
  justifyContent: 'center',
}

export default class CartPanel extends React.Component {

  static propTypes = {
    cart: PropTypes.object,
    cartProducts: PropTypes.array,
    festivals: PropTypes.array,
    removeCartProduct: PropTypes.func,
    selectFestival: PropTypes.func,
    updateQuantity: PropTypes.func,
    onCheckout: PropTypes.func,
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

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }

  initialStyle() {
    return {
      padding: 0,
      width: spring(0, { stiffness: 150, damping: 20 }),
      height: spring(600, { stiffness: 100, damping: 20 }),
      right: spring(0, { stiffness: 100, damping: 10 }),
    }
  }

  handleClick(e) {
    const { open } = this.state
    if (!this.node.contains(e.target) && this.state.open) {
      this.setState({
        open: !open,
      })
    }
    if (e.target.id === 'open-cart') {
      this.setState({
        open: !open,
      })
    }
  }

  finalStyle() {
    return {
      padding: 20,
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

  showChildren() {
    const { cartProducts, updateQuantity, removeCartProduct } = this.props
    return (cartProducts.map((cartProduct) => (
      <CartItem
        updateQuantity={updateQuantity}
        removeCartProduct={removeCartProduct}
        key={cartProduct.id}
        cartProduct={cartProduct}
      />
    )))
  }

  render() {
    const { open } = this.state
    const style = !open ? this.initialStyle() : this.finalStyle()
    // open ? this.dimDoc() : this.undimDoc()
    return (
      <Motion style={style} >
        {({ width, height, right, padding }) => (
          <div
            ref={node => this.node = node}
            style={{
              ...styler,
              width: width,
              height: height,
              right: right,
              padding: padding,
            }}
          >
            {open ? this.showChildren() : null}
          </div>
          )
        }
      </Motion>
    )
  }
}
