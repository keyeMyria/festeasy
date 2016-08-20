import React, { PropTypes } from 'react';
import {
  Input,
  Grid,
  Column,
  Button,
  Divider,
  Image,
} from 'semantic-react'
import Navbar from 'main/components/navbar.jsx'
import logo from 'fe_logo.png'


export default class Main extends React.Component {
  static propTypes = {
    children: PropTypes.object.isRequired,
  }

  render() {
    return (
      <div>
        <Navbar />
        <div className="ui container">
          <Grid columns={3} centered>
            <Column width={4}>
              <Image
                style={{ maxHeight: 70 }}
                src={logo}
              />
            </Column>
            <Column width={8}>
              <Input
                fluid
                size="big"
                icon="search"
                placeholder="What are you looking for?"
              />
            </Column>
            <Column width={4} />
          </Grid>
        </div>
        <Divider />
        {this.props.children}
        <div>
          Footer stuff
        </div>
      </div>
    )
  }
}
