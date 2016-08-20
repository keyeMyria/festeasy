import React from 'react'
import { Link } from 'react-router'
import {
  Header,
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
        <br />
        <br />
        <br />
        <br />
        <br />
        <Grid centered>
          <Column>
            <Link
              to="/how-it-works"
              className="ui yellow massive button"
            >
              How it Works
            </Link>
          </Column>
        </Grid>
      </div>
    )
  }
}
