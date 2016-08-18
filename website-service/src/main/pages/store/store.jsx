import React, { PropTypes } from 'react'
import { Form, Input, Button, Divider } from 'semantic-react'


class ProductSearch extends React.Component {
  static propTypes = {
    onClick: PropTypes.func.isRequired,
    searchTerm: PropTypes.string,
  }

  constructor(props) {
    super(props)
    this.state = {
      searchTerm: props.searchTerm || '',
    }
    this.onSubmit = this.onSubmit.bind(this)
    this.onChange = this.onChange.bind(this)
  }

  onSubmit(e) {
    e.preventDefault()
    this.props.onClick(this.state.searchTerm)
  }

  onChange(e) {
    this.setState({ searchTerm: e.target.value })
  }

  render() {
    const { searchTerm } = this.state
    return (
      <Form onSubmit={this.onSubmit}>
        <Input
          type="text"
          placeholder="Search products..."
          value={searchTerm}
          onChange={this.onChange}
        />
        <Button>Search</Button>
      </Form>
    )
  }
}


export default class Store extends React.Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    children: PropTypes.any.isRequired,
    location: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.onSearch = this.onSearch.bind(this)
  }

  onSearch(term) {
    const path = term === '' ? '' : '?search='.concat(term)
    this.context.router.push('/store'.concat(path))
  }

  render() {
    const { search } = this.props.location.query
    return (
      <div>
        <div className="ui container">
          <ProductSearch onClick={this.onSearch} searchTerm={search} />
          <Divider />
          {this.props.children}
        </div>
      </div>
    )
  }
}
