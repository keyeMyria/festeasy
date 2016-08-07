import React, { PropTypes } from 'react'
import MyInput from 'utils/myInput.jsx'


export default class MyStatefulInput extends React.Component {
  static propTypes = {
    initialValue: PropTypes.any.isRequired,
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
      <MyInput
        onChange={this.onChange}
        value={value}
        {...filteredProps}
      />
    )
  }
}
