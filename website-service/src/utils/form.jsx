import React, { PropTypes, Component } from 'react'
import { Header, Form as SRF, Input, Field, Button } from 'semantic-react'


class BasicForm extends Component {
  static contextTypes = {
    addNotification: PropTypes.func.isRequired,
  }

  static propTypes = {
    fields: PropTypes.array.isRequired,
    onSubmit: PropTypes.func.isRequired,
    header: PropTypes.any,
  }

  constructor(props) {
    super(props)
    const fields = {}
    props.fields.forEach(f => {
      fields[f.attr] = f.initialValue
    })
    this.state = {
      fields,
    }
  }

  onSubmit = e => {
    e.preventDefault()
    this.setState({ isLoading: true })
    const s = this.props.onSubmit(this.state.fields)
    s.then(() => {
      this.setState({ isLoading: false })
      this.context.addNotification({
        'message': 'Success!',
        'level': 'success',
      })
    })
    s.catch(() => {
      this.setState({ isLoading: false })
      this.context.addNotification({
        'message': 'Error :(',
        'level': 'error',
      })
    })
  }

  handleChange = (attr, value) => {
    const fields = Object.assign(this.state.fields)
    fields[attr] = value
    this.setState({ fields })
  }

  getField = f => (
    <Field key={f.attr}>
      {f.label ? <label htmlFor={f.attr}>{f.label}</label> : ''}
      {f.component ?
        <f.component
          name={f.attr}
          onChange={value => this.handleChange(f.attr, value)}
          value={this.state.fields[f.attr]}
          {...f.componentProps}
        />
        :
        <Input
          name={f.attr}
          onChange={e => this.handleChange(f.attr, e.target.value)}
          value={this.state.fields[f.attr]}
          {...f.componentProps}
        />
      }
    </Field>
  )

  render() {
    return (
      <div>
        {this.props.header ? <Header>{this.props.header}</Header> : ''}
        <SRF onSubmit={this.onSubmit} loading={this.state.isLoading}>
          {this.props.fields.map((f) => this.getField(f))}
          <Button
            state={this.state.isLoading ? 'loading' : ''}
            color="blue"
            type="submit"
          >
            Submit
          </Button>
        </SRF>
      </div>
    )
  }
}

module.exports = {
  BasicForm,
}
