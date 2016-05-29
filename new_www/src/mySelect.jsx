import React, { PropTypes } from 'react'
import { Select } from 'semantic-react'


export default class MySelect extends React.Component {
  constructor(props) {
    super(props)
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
        placeholder={placeholder}
        onClick={() => this.setState({ active: true })}
        onRequestClose={() => this.setState({ active: false })}
        onSearchStringChange={string => this.setState({ searchString: string })}
        searchString={searchString}
        onSelectChange={val => this.props.updateSelected(val)}
      >
        {options.map((option) => (
          option
        ))}
      </Select>
    )
  }
}

MySelect.propTypes = {
  options: PropTypes.array.isRequired,
  updateSelected: PropTypes.func.isRequired,
  placeholder: PropTypes.string,
  selected: PropTypes.array,
  fluid: PropTypes.bool,
}
