import React, { PropTypes, Component } from 'react'
import { Select as SRSelect } from 'semantic-react'


class MultiSelect extends Component {
  static propTypes = {
    options: PropTypes.array.isRequired,
    onChange: PropTypes.func.isRequired,
    value: PropTypes.any,
    props: PropTypes.object,
    placeholder: PropTypes.string,
  }

  constructor() {
    super()
    this.state = {
      active: false,
      searchString: '',
    }
  }

  render() {
    const { active, searchString } = this.state
    const { placeholder, options, value, onChange } = this.props
    return (
      <SRSelect
        selection
        multiple
        active={active}
        selected={value || []}
        placeholder={searchString ? '' : placeholder}
        onClick={() => this.setState({ active: true })}
        onRequestClose={() => this.setState({ active: false })}
        onSearchStringChange={string => this.setState({ searchString: string })}
        searchString={searchString}
        onSelectChange={val => {
          onChange(val)
        }}
        {...this.props.props}
      >
        {options.map((option) => (
          option
        ))}
      </SRSelect>
    )
  }
}


class SingleSelect extends Component {
  static propTypes = {
    options: PropTypes.array.isRequired,
    onChange: PropTypes.func.isRequired,
    value: PropTypes.any,
    props: PropTypes.object,
    placeholder: PropTypes.string,
  }

  constructor() {
    super()
    this.state = {
      active: false,
      searchString: '',
    }
  }

  render() {
    const { active, searchString } = this.state
    const { placeholder, options, value, onChange } = this.props
    return (
      <SRSelect
        selection
        active={active}
        selected={value ? [value] : []}
        placeholder={searchString ? '' : placeholder}
        onClick={() => this.setState({ active: true })}
        onRequestClose={() => this.setState({ active: false })}
        onSearchStringChange={string => this.setState({ searchString: string })}
        searchString={searchString}
        onSelectChange={val => {
          onChange(val[0])
        }}
        {...this.props.props}
      >
        {options.map((option) => (
          option
        ))}
      </SRSelect>
    )
  }
}

module.exports = {
  SingleSelect,
  MultiSelect,
}
