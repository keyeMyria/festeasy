import React, { PropTypes } from 'react'


class ProductSearch extends React.Component {
  static propTypes = {
    onClick: PropTypes.func.isRequired,
  }

  constructor() {
    super()
    this.state = {
      searchTerm: '',
    }
    this.onClick = this.onClick.bind(this)
    this.onChange = this.onChange.bind(this)
  }

  onClick() {
    this.props.onClick(this.state.searchTerm)
  }

  onChange(e) {
    this.setState({ searchTerm: e.target.value })
  }

  render() {
    const { searchTerm } = this.state
    return (
      <div className="ui fluid action input">
        <input
          type="text"
          placeholder="Search products..."
          value={searchTerm}
          onChange={this.onChange}
        />
        <button className="ui button" onClick={this.onClick}>Search</button>
      </div>
    )
  }
}


export default class Store extends React.Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  constructor() {
    super()
    this.onSearch = this.onSearch.bind(this)
  }

  onSearch(term) {
    this.context.router.push(`/store?search=${term}`)
  }

  render() {
    return (
      <div>
        <h1 className="ui center aligned header">Store</h1>
        <ProductSearch onClick={this.onSearch} />
        <div className="ui divider" />
        {this.props.children}
      </div>
    )
  }
}
