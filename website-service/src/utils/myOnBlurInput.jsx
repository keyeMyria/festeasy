import React, { PropTypes } from 'react'
import { Input } from 'semantic-react'


export default class MyOnBlurInput extends React.Component {
  static propTypes = {
    initialValue: PropTypes.any.isRequired,
    onBlur: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      value: this.props.initialValue,
    }
    this.onChange = this.onChange.bind(this)
  }

  onChange(e) {
    this.setState({ value: e.target.value })
  }

  render() {
    const { value } = this.state
    const filteredProps = Object.assign({}, this.props)
    delete filteredProps.initialValue
    return (
      <Input
        {...filteredProps}
        value={value}
        onChange={this.onChange}
        onBlur={this.props.onBlur}
      />
    )
  }
}
