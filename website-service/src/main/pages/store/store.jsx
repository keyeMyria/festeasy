import React, { PropTypes } from 'react'


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
      <form className="ui form" onSubmit={this.onSubmit}>
        <input
          type="text"
          placeholder="Search products..."
          value={searchTerm}
          onChange={this.onChange}
        />
        <button className="ui button">Search</button>
      </form>
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
        <h1 className="ui center aligned header">Store</h1>
        <ProductSearch onClick={this.onSearch} searchTerm={search} />
        <div className="ui divider" />
        {this.props.children}
      </div>
    )
  }
}
