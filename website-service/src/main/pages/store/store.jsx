import React, { PropTypes } from 'react'
import NavLink from 'common/navLink.jsx'


export default class Store extends React.Component {
  static contextTypes = {
    axios: PropTypes.func.isRequired,
  }

  static propTypes = {
    children: PropTypes.any.isRequired,
  }

  constructor() {
    super()
    this.state = {
      categories: [],
    }
  }

  componentDidMount() {
    this.fetchCategories()
  }

  fetchCategories = () => {
    this.context.axios.get('v1/categories')
    .then((r) => {
      this.setState({
        categories: r.data.data,
      })
    })
  }

  render() {
    return (
      <div>
        <div className="ui container">
          <div className="ui two column grid">
            <div className="four wide column">
              <div className="ui vertical pointing menu">
                {this.state.categories.map(c => (
                  <NavLink key={c.id} to={`/store/categories/${c.name}`}>{c.name}</NavLink>
                ))}
              </div>
            </div>
            <div className="twelve wide column">
              {this.props.children}
            </div>
          </div>
        </div>
      </div>
    )
  }
}
