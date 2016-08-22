import React, { PropTypes } from 'react'
import { Link } from 'react-router'
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
      <div className="ui inverted vertical footer segment">
        <div className="ui center aligned container">
          <div className="ui stackable inverted divided grid">
            <div className="seven wide column">
              <h4 className="ui inverted header">
                Some links here
              </h4>
              <div className="ui inverted link list">
                <Link className="item" to="/store">Facebook</Link>
                <Link className="item" to="/store">Twitter</Link>
                <Link className="item" to="/store">Instagram</Link>
              </div>
            </div>
            <div className="seven wide column">
              <h4 className="ui inverted header">
                Fest Easy
              </h4>
            </div>
          </div>
          <div className="ui horizontal inverted small divided link list">
            <Link className="item" to="/contact-us">Contact Us</Link>
            <Link className="item" to="/terms-and-conditions">Terms and Conditions</Link>
            <Link className="item" to="/privacy-policy">Privacy Polidy</Link>
          </div>
        </div>
      </div>
    )
  }
}

export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
    location: PropTypes.object.isRequired,
  }

  render() {
    const style = {
      paddingTop: 70,
      display: 'flex',
      minHeight: '100vh',
      flexDirection: 'column',
    }
    return (
      <div>
        <Navbar />
        <div style={style}>
          <Bar location={this.props.location} />
          <Divider />
          <div style={{ flex: 1, paddingBottom: 40 }}>
            {this.props.children}
          </div>
          <Footer />
        </div>
      </div>
    )
  }
}
