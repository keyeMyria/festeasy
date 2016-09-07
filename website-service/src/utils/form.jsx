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
    isLoading: PropTypes.bool,
  }

  onSubmit = (e) => {
    e.preventDefault()
    this.props.onSubmit(this.state)
    .then(() => {
      this.context.addNotification({
        'message': 'Success!',
        'level': 'success',
      })
    })
    .catch(() => {
      this.context.addNotification({
        'message': 'Error :(',
        'level': 'error',
      })
    })
  }

  getField = f => (
    <Field key={f.attr}>
      {f.label ? <label htmlFor={f.attr}>{f.label}</label> : ''}
      {f.component ?
        <f.component
          name={f.attr}
          onChange={value => this.setState({ [f.attr]: value })}
          value={this.state ? this.state[f.attr] : null}
          {...f.componentProps}
        />
        :
        <Input
          name={f.attr}
          onChange={e => this.setState({ [f.attr]: e.target.value })}
          value={this.state ? this.state[f.attr] : f.initialValue}
          {...f.componentProps}
        />
      }
    </Field>
  )

  render() {
    return (
      <div>
        {this.props.header ? <Header>{this.props.header}</Header> : ''}
        <SRF onSubmit={this.onSubmit} loading={this.props.isLoading}>
          {this.props.fields.map((f) => this.getField(f))}
          <Button
            state={this.props.isLoading ? 'loading' : ''}
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
