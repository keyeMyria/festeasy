import React, { PropTypes } from 'react';
import { TransitionMotion, Motion, spring } from 'react-motion';
import { Button } from 'semantic-react'

/* eslint-disable react/self-closing-comp */


const panelWidth = 200
const stayOpen = true
const styler = {
  position: 'absolute',
  zIndex: 5,
  border: '1px solid',
  borderColor: '#6AA0D5',
  // borderRadius: '10px',
  overflowX: 'hidden',
  WebkitBoxSizing: 'border-box',
  boxSizing: 'border-box',
  backgroundColor: 'white',
  cursor: 'pointer',
  // boxShadow: '-5px 2px 5px #afafaf',
  justifyContent: 'center',
}

export default class HoverMenu extends React.Component {

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
    this.handleClick = this.handleClick.bind(this)
  }

  componentWillMount() {
    document.addEventListener('click', this.handleClick, false)
  }

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }

  getAttr(ob, attr) {
    return (ob ? ob[attr] : null)
  }

  initialStyle() {
    const { posX, posY } = this.state
    return {
      padding: 0,
      width: spring(window.innerWidth, { stiffness: 150, damping: 20 }),
      height: spring(0, { stiffness: 300, damping: 20 }),
      left: spring(0, { stiffness: 350, damping: 10 }),
      top: spring(95, { stiffness: 350, damping: 10 }),
    }
  }

  finalStyle() {
    return {
      padding: 20,
      width: spring(window.innerWidth, { stiffness: 150, damping: 26 }),
      height: spring(350, { stiffness: 300, damping: 20 }),
      left: spring(0, { stiffness: 100, damping: 10 }),
      top: spring(95, { stiffness: 150, damping: 10 }),
    }
  }

  handleClick(e) {
    console.log('opeoing: ', e)
    const { open } = this.state
    if (!stayOpen && !this.node.contains(e.target) && this.state.open) {
      this.setState({
        open: !open,
      })
    }
    if (e.target.id === 'show-products') {
      this.setState({
        open: !open,
      })
    }
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


  render() {
    const { open } = this.state
    const style = !open ? this.initialStyle() : this.finalStyle()
    return (
      <Motion style={style} >
        {({ width, height, left, padding, top }) => (
          <div
            /* eslint-disable */
            ref={node => this.node = node}
            /* eslint-enable */
            style={{
              ...styler,
              width: width,
              height: height,
              left: left,
              padding: padding,
              top: top,
            }}
          >
            {open ?
              <div>
                <div className="ui items">
                  <div>
                    hello
                  </div>
                  <div>
                    there
                  </div>
                  <div className="item">
                    <div className="ui hidden divider" ></div>
                  </div>
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
