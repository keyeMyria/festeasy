import React, { PropTypes } from 'react'
import {
  Header,
  Button,
  Content,
  Grid,
  Row,
  Column,
  Description,
  Cards,
  Card,
} from 'semantic-react'


export default class FestivalsContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      festivals: null,
    }
    this.fetchFestivals = this.fetchFestivals.bind(this)
  }

  componentDidMount() {
    this.fetchFestivals()
  }

  fetchFestivals() {
    this.context.store.findAll(
      'festival',
    )
    .then((festivals) => {
      this.setState({ festivals })
    })
  }

  render() {
    let festivals = []
    if (this.state.festivals) {
      festivals = this.state.festivals.map((f) => (
        <Card
          style={{ height: 200 }}
        >
          <Content>
            <Header>
              {f.name}
            </Header>
            <Description>
              {f.description}
            </Description>
          </Content>
        </Card>
      ))
    }
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
            {festivals}
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
