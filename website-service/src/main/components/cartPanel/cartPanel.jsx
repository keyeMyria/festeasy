import React, { PropTypes } from 'react';
import { TransitionMotion, Motion, spring } from 'react-motion';
import { Button } from 'semantic-react'
import CartItem from './cartItem.jsx'

/* eslint-disable react/self-closing-comp */


const panelWidth = 400
const bottom = window.innerHeight - 20
const top = 40
const stayOpen = true
const styler = {
  position: 'fixed',
  zIndex: 5,
  paddingTop: '60px',
  border: '1px solid',
  borderColor: '#6AA0D5',
  borderRadius: '10px',
  overflowX: 'hidden',
  WebkitBoxSizing: 'border-box',
  boxSizing: 'border-box',
  backgroundColor: 'white',
  cursor: 'pointer',
  padding: 20,
  boxShadow: '-5px 2px 5px #afafaf',
  justifyContent: 'center',
  top: top,
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
    document.getElementById('main').style.transition = 'padding-right 0.5s'
  }

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }

  getAttr(ob, attr) {
    return (ob ? ob[attr] : null)
  }

  initialStyle() {
    return {
      width: spring(panelWidth * 1, { stiffness: 150, damping: 20 }),
      height: spring(window.innerHeight - top, { stiffness: 100, damping: 20 }),
      right: spring(-800, { stiffness: 150, damping: 10 }),
    }
  }

  finalStyle() {
    return {
      width: spring(panelWidth * 2, { stiffness: 150, damping: 32 }),
      height: spring(window.innerHeight - top, { stiffness: 100, damping: 20 }),
      right: spring(-400, { stiffness: 100, damping: 10 }),
    }
  }

  handleClick(e) {
    const { open } = this.state
    if (!stayOpen && !this.node.contains(e.target) && this.state.open) {
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
      paddingLeft: spring(400, { stiffness: 450, damping: 26 }),
      paddingRight: spring(0, { stiffness: 450, damping: 26 }),
    }
  }

//  TODO: seperate into functional paradymes
  showHeader() {
    const { cart } = this.props
    return (
      <div className="ui grid">
        <div className="eight wide column">
          <div className="row">
            <div className="ui header">
              Your Festeasy Cart for:
            </div>
          </div>
          <div className="row">
            <div className="ui header">
              {cart.festival ? cart.festival.name : 'No festival selected'}
            </div>
            <div className="ui header">
              {/* {cart.festival ? cart.festival.starts_on : ''} */}
            </div>
          </div>
          <div className="row">
            <div className="ui divider">
            </div>
          </div>
        </div>
        <div className="eight wide column">
        </div>
      </div>
    )
  }
  showCartItems() {
    const { cartProducts, updateQuantity, removeCartProduct } = this.props
    return (
      <TransitionMotion
        willEnter={this.willEnter}
        willLeave={this.willLeave}
        styles={cartProducts.map(cp => ({
          key: cp.id,
          data: cp,
          style: { paddingLeft: spring(0, { stiffness: 150, damping: 36 }),
            paddingRight: spring(400, { stiffness: 150, damping: 36 }) },
        })
        )}
      >
        {interpolatedStyles => (
          <div>
            {
              interpolatedStyles.map(config => (
                <div style={{ ...config.style }}>
                  <CartItem
                    updateQuantity={updateQuantity}
                    removeCartProduct={removeCartProduct}
                    key={config.id}
                    cartProduct={config.data}
                  />
                </div>
              )
              )
            }
          </div>
        )}
      </TransitionMotion>
    )
  }

  showCartTotalBox() {
    const { cart } = this.props
    const headings = [
      'Total Cost:',
      'no. unique items:']
    return (
      <div>
        <div
          style={{
            position: 'fixed',
            top: bottom - 90,
            backgroundColor: 'white',
            border: '1px solid',
            borderColor: '#6AA0D5',
            borderRadius: '20px',
            height: '109px',
            padding: '10px'
          }}
          className="five wide column"
        >
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
          <div className="ui center aligned" style={{ width: `${panelWidth - 60}px` }}>
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
      </div>
    )
  }
  render() {
    const { open } = this.state
    const style = !open ? this.initialStyle() : this.finalStyle()
    /* eslint-disable */
    open ? document.getElementById('main').style.paddingRight = `${panelWidth}px`
      : document.getElementById('main').style.paddingRight = '0px'
    /* eslint-enable */
    return (
      <Motion style={style} >
        {({ width, height, right, padding }) => (
          <div
            /* eslint-disable */
            ref={node => this.node = node}
            /* eslint-enable */
            style={{
              ...styler,
              width: width,
              height: height,
              right: right,
            }}
          >
            <div>
              {this.showHeader()}
            </div>
            <div className="ui hidden divider" ></div>
            <div>
              {this.showCartItems()}
            </div>
            <div>
              {this.showCartTotalBox()}
            </div>
          </div>
          )
        }
      </Motion>
      )
  }
  }
