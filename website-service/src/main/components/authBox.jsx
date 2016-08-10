import React, { PropTypes } from 'react'
import { Header, Grid, Column, Segment } from 'semantic-react'


export default class AuthBox extends React.Component {
  static propTypes = {
    title: PropTypes.any.isRequired,
    children: PropTypes.any.isRequired,
  }

  render() {
    const { title, children } = this.props
    return (
      <Grid centered>
        <Column width={6}>
          <Segment>
            <Header>{title}</Header>
            {children}
          </Segment>
        </Column>
      </Grid>
    )
  }
}
