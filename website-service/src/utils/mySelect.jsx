import React, { PropTypes } from 'react'
import { Select } from 'semantic-react'


export default class MySelect extends React.Component {
  static propTypes = {
    options: PropTypes.array.isRequired,
    updateSelected: PropTypes.func.isRequired,
    placeholder: PropTypes.string,
    selected: PropTypes.array,
    fluid: PropTypes.bool,
  }

  constructor() {
    super()
    this.state = {
      active: false,
      searchString: '',
    }
  }

  render() {
    const { fluid, options, placeholder, selected } = this.props
    const { active, searchString } = this.state
    return (
      <Select
        search
        selection
        fluid={fluid}
        active={active}
        selected={selected}
        placeholder={searchString ? '' : placeholder}
        onClick={() => this.setState({ active: true })}
        onRequestClose={() => this.setState({ active: false })}
        onSearchStringChange={string => this.setState({ searchString: string })}
        searchString={searchString}
        onSelectChange={val => {
          if (typeof this.props.updateSelected === 'function') {
            this.props.updateSelected(val)
            this.setState({ active: false })
          } else {
            this.props.updateSelected(val).then(() => {
              this.setState({ active: false })
            })
          }
        }}
      >
        {options.map((option) => (
          option
        ))}
      </Select>
    )
  }
}
