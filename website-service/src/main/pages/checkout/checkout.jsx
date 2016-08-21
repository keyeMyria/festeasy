import React, { PropTypes } from 'react'
import { Segment, Header, Content, Steps, Step, Description } from 'semantic-react'


export default class Checkout extends React.Component {
  static propTypes = {
    children: PropTypes.any.isRequired,
    location: PropTypes.object.isRequired,
  }

  render() {
    const { pathname } = this.props.location
    const steps = [
      {
        title: 'Cart',
        completed: true,
        description: 'Choose your products and festival',
        active: false,
      }, {
        title: 'Review',
        completed: false,
        description: 'Review your cart',
        active: pathname === '/checkout/review',
      }, {
        title: 'Payment',
        completed: false,
        description: 'Make payment',
        active: pathname === '/checkout/payment',
      }, {
        title: 'Confirmation',
        completed: false,
        description: 'Recieve payment confirmation',
      },
    ]
    return (
      <div className="ui container">
        <Header aligned="center">Checkout</Header>
        <Steps ordered fluid equalWidths>
          {steps.map((step) => (
            <Step
              key={step.title}
              completed={step.completed || false}
              active={step.active || false}
            >
              <Content>
                <div className="title">{step.title}</div>
                <Description>{step.description}</Description>
              </Content>
            </Step>
          ))}
        </Steps>
        <Segment>
          {this.props.children}
        </Segment>
      </div>
    )
  }
}
