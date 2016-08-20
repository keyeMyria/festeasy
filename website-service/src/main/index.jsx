import React, { PropTypes } from 'react';
import {
  Input,
  Grid,
  Column,
  Divider,
  Image,
  Form,
} from 'semantic-react'
import Navbar from 'main/components/navbar.jsx'
import logo from 'fe_logo.png'
import CartContainer from 'main/components/cart/cartContainer.jsx'
import CartPanel from 'main/components/cartPanel/cartPanel.jsx'
import HoverMenu from 'main/components/hoverMenu/hoverMenu.jsx'


class Bar extends React.Component {

  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    location: PropTypes.object.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      searchTerm: props.location.query.term || '',
    }
    this.onSubmit = this.onSubmit.bind(this)
    this.onChange = this.onChange.bind(this)
  }

  componentWillReceiveProps(nextProps) {
    if (!nextProps.location.query.term) {
      this.setState({ searchTerm: '' })
    }
  }

  onSubmit(e) {
    e.preventDefault()
    const { searchTerm } = this.state
    if (searchTerm) {
      this.context.router.push({
        pathname: '/search',
        query: { term: searchTerm },
      })
    }
  }

  onChange(e) {
    this.setState({ searchTerm: e.target.value })
  }


  render() {
    return (
      <div className="ui container">
        <Grid columns={3} centered>
          <Column width={4}>
            <Image
              style={{ maxHeight: 70 }}
              src={logo}
            />
          </Column>
          <Column width={8}>
            <Form onSubmit={this.onSubmit}>
              <Input
                fluid
                size="big"
                icon="search"
                onChange={this.onChange}
                value={this.state.searchTerm}
                placeholder="What are you looking for?"
              />
            </Form>
          </Column>
          <Column width={4} />
        </Grid>
      </div>
      )
  }
  }


class Footer extends React.Component {
  render() {
    return (
      <div className="ui container">
        Footer stuff
      </div>
    )
  }
}


export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
    location: PropTypes.object.isRequired,
  }

  static contextTypes = {
    authDetails: PropTypes.object,
  }

  render() {
    const { authDetails } = this.context
    return (
      <div>
        <Navbar />
        {authDetails ? (
          <div>
            <HoverMenu />
            <CartContainer>
              <CartPanel />
            </CartContainer>
          </div>
        ) : null}
        <div className="ui one column stackable center aligned page grid">
          <button
            className="ui tiny blue button center aligned"
            id="show-products"
          >Categories</button>
        </div>
        <div className="ui hidden divider"></div>
        <Bar location={this.props.location} />
        <div id="main">
          <Divider />
          {this.props.children}
          <Footer />
        </div>
      </div>
    )
  }
}
