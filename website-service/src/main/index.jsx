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

  render() {
    return (
      <div>
        <Navbar />
        <Bar location={this.props.location} />
        <Divider />
        {this.props.children}
        <Footer />
      </div>
    )
  }
}
