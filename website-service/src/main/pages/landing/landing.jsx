import React from 'react';
import {
  Header,
  Button,
  Content,
  Grid,
  Row,
  Column,
  Cards,
  Card,
} from 'semantic-react'


class Lead extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: 'url(\'/images/jumbo_1.png\')',
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


class Festival extends React.Component {
  render() {
    return (
      <div>
        <Header
          aligned="center"
          size="huge"
        >
          find your festival
        </Header>
        <Grid>
          <Row>
            <Column aligned="center">
              <p>
                We offer our services to every major festival in the Western Cape.
              </p>
            </Column>
          </Row>
          <Row>
            <Column aligned="center">
              <p>
                As our customer base grows, so will our festival selection
                , as we aim to move to every festival in South Africa and... the World.
              </p>
            </Column>
          </Row>
        </Grid>
        <div className="ui container">
          <Cards className="three">
            {[1, 2, 3, 4, 5, 6, 7, 8].map(() => (
              <Card
                style={{ height: 200 }}
              >
                <Content>
                  <Header>
                    Some festival
                  </Header>
                </Content>
              </Card>
            ))}
          </Cards>
          <Grid centered>
            <Column>
              <Button
                size="large"
                color="yellow"
              >
                See All Festivals
              </Button>
            </Column>
          </Grid>
        </div>
      </div>
    )
  }
}


class Shop extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: 'url(\'/images/voss.jpg\')',
          backgroundSize: '100%',
          height: 600,
        }}
      >
        <Header
          style={{ color: 'white' }}
          aligned="center"
          size="large"
        >
          shop
        </Header>
      </div>
    )
  }
}


class Community extends React.Component {
  render() {
    return (
      <div>
        <Header
          aligned="center"
          size="large"
        >
          community
        </Header>
      </div>
    )
  }
}


export default class Landing extends React.Component {
  render() {
    return (
      <div>
        <Lead />
        <Festival />
        <Shop />
        <Community />
      </div>
    )
  }
}
