import React, { PropTypes } from 'react';
import { TransitionMotion, Motion, spring } from 'react-motion';
import CartItem from './cartItem.jsx'
import { Button } from 'semantic-react'

// import { MenuItem } from 'semantic-react'
// import { Tab } from 'semantic-react'
// import Tabs from '../components/sidePanel/tabs.jsx'
// import TabMenu from '../components/sidePanel/tabmenu.jsx'
// import Tab from '../components/sidePanel/tab.jsx'

// import CartItem from './cartItem.jsx'
const panelWidth = 400
const styler = {
  position: 'fixed',
  zIndex: 5,
  paddingTop: '60px',
  border: '1px solid',
  borderColor: '#6AA0D5',
  borderRadius: '10px',
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
    document.getElementById("main").style.transition = 'padding-right 0.5s'
  }

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }

  initialStyle() {
    return {
      padding: 0,
      width: spring(panelWidth * 2, { stiffness: 150, damping: 20 }),
      height: spring(600, { stiffness: 100, damping: 20 }),
      right: spring(-800, { stiffness: 150, damping: 10 }),
    }
  }

  handleClick(e) {
    const { open } = this.state
    // if (!this.node.contains(e.target) && this.state.open) {
    //   this.setState({
    //     open: !open,
    //   })
    // }
    if (e.target.id === 'open-cart') {
      this.setState({
        open: !open,
      })
    }
  }

  finalStyle() {
    return {
      padding: 20,
      width: spring(panelWidth*2, { stiffness: 150, damping: 26 }),
      height: spring(window.innerHeight-70, { stiffness: 100, damping: 20 }),
      right: spring(-400, { stiffness: 100, damping: 10 }),
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
  willEnter() {
    console.log('calling willEnter: ')
    return {
      paddingLeft: 400,
      paddingRight: 0,
    }
  }
  willLeave() {
    return {
      paddingLeft: spring(400),
      paddingRight: spring(0),
    }
  }
  showCartItems() {
    const { cartProducts, updateQuantity, removeCartProduct } = this.props
    return (
      <TransitionMotion willEnter={this.willEnter} willLeave={this.willLeave}
        styles={cartProducts.map(cp => ({
          key: cp.id,
          data: cp,
          style: { paddingLeft: spring(0, { stiffness: 150, damping: 36 }), paddingRight: spring(400, { stiffness: 150, damping: 36 }) },
        })
        )}>
        {interpolatedStyles => (
          <div>
            {
              interpolatedStyles.map(config => {
                console.log('config: ', config)
                return (
                  <div style={{ ...config.style }}>
                    <CartItem
                      updateQuantity={updateQuantity}
                      removeCartProduct={removeCartProduct}
                      key={config.id}
                      cartProduct={config.data}
                    />
                  </div>
                )
              })
            }
          </div>
        )}
      </TransitionMotion>
        )
  }

  getAttr(ob, attr) {
    return (ob ? ob[attr] : null)
  }
  showCartTotalBox() {
    const { cart } = this.props
    const headings = [
      'Total Cost:',
      'no. unique items:']
    return (
      <div style={{ height: '160px' }}>
        <div className="ui grid" >
          <div className="eleven wide column" >
            {headings.map((heading) => (
              <div className="row" >
                {heading}
              </div>
            ))}
          </div>
          <div className="five wide column" >
            <div className="row" >
              {this.getAttr(cart, 'total_rands')}
            </div>
            <div className="row" >
              {this.getAttr(cart.cart_products, 'length')}
            </div>
          </div>
        </div>
        <div className="ui center aligned" style={{ width: `${panelWidth-40}px` }}>
          <Button
            onClick={() => {
              this.props.onCheckout(); this.setState({
                open: !open,
              })
            }
            }
            className="fluid"
          >CHECKOUT</Button>
        </div>
      </div>
    )
  }
  render() {
    const { open } = this.state
    const style = !open ? this.initialStyle() : this.finalStyle()
    // open ? this.dimDoc() : this.undimDoc()
    open ? document.getElementById("main").style.paddingRight = `${panelWidth}px`
      : document.getElementById("main").style.paddingRight = "0px"
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
            {open ?
              <div>

                <div className="ui items">
                  <div>
                    {this.showCartItems()}
                  </div>
                  <div className="item">
                    <div className="ui hidden divider" ></div>
                  </div>
                </div>
                <div
                  style={{
                    position: 'fixed',
                    top: height - 60,
                    backgroundColor: 'white',
                    width: width,
                    height: '84px',
                  }}
                  className="six wide column"
                >
                  <div className="ui divider" ></div>
                  {this.showCartTotalBox()}
                </div>
              </div>
            : null}
          </div>
          )
        }
      </Motion>
          )
        }
}
