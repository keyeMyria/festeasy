import React, { PropTypes, Component } from 'react'
import { Header, Form as SRF, Input, Field, Button } from 'semantic-react'


class BasicForm extends Component {
  static propTypes = {
    onSubmit: PropTypes.func,
    fields: PropTypes.array,
    header: PropTypes.any,
  }

  onSubmit = (e) => {
    e.preventDefault()
    this.props.onSubmit(this.state)
  }

  getField = f => (
    <Field key={f.attr}>
      {f.label ? <label htmlFor={f.attr}>{f.label}</label> : ''}
      {f.control ?
        <f.control
          name={f.attr}
          onChange={value => this.setState({ [f.attr]: value })}
          value={this.state ? this.state[f.attr] : null}
          {...f.props}
        />
        :
        <Input
          name={f.attr}
          onChange={e => this.setState({ [f.attr]: e.target.value })}
          {...f.props}
        />
      }
    </Field>
  )


  render() {
    return (
      <div>
        {this.props.header ? <Header>{this.props.header}</Header> : ''}
        <SRF onSubmit={this.onSubmit}>
          {this.props.fields.map((f) => this.getField(f))}
          <Button color="blue" type="submit">Submit</Button>
        </SRF>
      </div>
    )
  }
}

module.exports = {
  BasicForm,
}
