import React, { PropTypes } from 'react'
import { Motion, spring } from 'react-motion';
import NavLink from 'common/navLink.jsx'
// import { Button } from 'semantic-react'

/* eslint-disable react/self-closing-comp */


// const panelWidth = 200
const stayOpen = true
const styler = {
  position: 'absolute',
  zIndex: 5,
  // border: '1px solid',
  // borderColor: '#6AA0D5',
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
  static contextTypes = {
    store: PropTypes.object,
  }

  constructor(props) {
    super(props);
    this.state = {
      active: 2,
      open: false,
      groups: null,
    }
    this.initialStyle = this.initialStyle.bind(this)
    this.finalStyle = this.finalStyle.bind(this)
    this.close = this.close.bind(this)
    this.handleClick = this.handleClick.bind(this)
    this.mapToLink = this.mapToLink.bind(this)
  }

  componentWillMount() {
    document.addEventListener('click', this.handleClick, false)
    this.getGroups()
  }

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClick, false)
  }
  getGroups() {
    const { store } = this.context
    store.findAll('group', {})
    .then((groups) =>
    this.setState({
      groups,
    })
  )
  }
  getAttr(ob, attr) {
    return (ob ? ob[attr] : null)
  }

  initialStyle() {
    return {
      padding: 0,
      width: spring(window.innerWidth, { stiffness: 150, damping: 20 }),
      height: 0,
      left: spring(0, { stiffness: 350, damping: 10 }),
      top: spring(88, { stiffness: 350, damping: 10 }),
    }
  }

  finalStyle() {
    return {
      padding: 20,
      width: spring(window.innerWidth, { stiffness: 150, damping: 26 }),
      height: spring(110, { stiffness: 300, damping: 30 }),
      left: spring(0, { stiffness: 100, damping: 10 }),
      top: spring(88, { stiffness: 150, damping: 10 }),
    }
  }

  handleClick(e) {
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

  mapToLink(arr) {
    // go through array
    // for each object in array, check the value for object, if array recursive, else print
    const links = []
    arr.forEach((heading) => {
      Object.keys(heading).forEach((subh) => {
        if (heading[subh] !== null && typeof heading[subh] === 'object') {
          this.mapToLink(heading[subh])
        } else {
          links.push(
            <div>
              {subh}
            </div>
          )
        }
      })
    })
    return (<div className="ui header">
      hello
    </div>)
  }

  render() {
    const { open, groups } = this.state
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
              <div className="ui container">
                <div className="ui grid">
                  {groups.map((g) => (
                    <div className="four wide column">
                      <div className="ui row">
                        <div className="ui blue header">
                          {g.name}
                        </div>
                        <div>
                          {g.categories.map((cat) => (
                            <div className="ui row">
                              <NavLink to={`/store/product-category/${cat.name}`}>
                                {cat.name}
                              </NavLink>
                            </div>
                            )
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
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
