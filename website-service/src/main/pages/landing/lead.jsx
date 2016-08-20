import React from 'react'
import {
  Header,
  Button,
  Grid,
  Column,
} from 'semantic-react'
import jumbo from 'jumbo_1.png'


export default class Lead extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: `url('${jumbo}')`,
          backgroundSize: '100%',
          height: 600,
        }}
      >
        <Header
          style={{ color: 'white' }}
          aligned="center"
          size="huge"
        >
          FESTIVALS, EASIER
        </Header>
        <Header
          style={{ color: 'white' }}
          aligned="center"
        >
          CHILLIN' ON THE DOORSTEP FOR YOUR CONVENIENCE
        </Header>
        <br />
        <br />
        <br />
        <br />
        <Grid centered>
          <Column>
            <Button
              size="large"
              color="yellow"
            >
              How it Workds
            </Button>
          </Column>
        </Grid>
      </div>
    )
  }
}
