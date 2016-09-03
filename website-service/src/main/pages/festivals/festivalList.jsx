import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { Cards, Card, Header, Description, Content, Date, Image } from 'semantic-react'
import { festivalShape } from 'utils/shapes.jsx'
import Page from 'utils/page.jsx'
import DateFormatter from 'utils/dateFormatter.jsx'
import SelectFestivalButton from 'main/components/selectFestivalButton.jsx'
import apiEndpoint from 'apiEndpoint.js'


class FestivalList extends React.Component {
  static propTypes = {
    festivals: PropTypes.arrayOf(
      festivalShape
    ).isRequired,
  }

  render() {
    const { festivals } = this.props
    const imageHeight = '250px'
    return (
      <Cards className="two">
        {festivals.map(festival => (
          <Card key={festival.id}>
            <Link to={`/festivals/${festival.id}`}>
              <div style={{ minHeight: imageHeight }}>
                {festival.image_id ?
                  <Image
                    centered
                    style={{ maxHeight: imageHeight, width: 'auto', height: 'auto' }}
                    alt="product thumbnail"
                    src={apiEndpoint.concat(
                      `v1/images/${festival.image_id}/image?height=250`
                    )}
                  /> : 'No thumbnail image'
                }
              </div>
            </Link>
            <Content>
              <Header>
                <Link to={`/festivals/${festival.id}`}>
                  {festival.name}
                </Link>
              </Header>
              <Content meta>
                <Date>
                  <DateFormatter date={festival.starts_on} />
                </Date>
              </Content>
              <Description>
                {festival.description}
              </Description>
              <SelectFestivalButton festival={festival} />
            </Content>
          </Card>
        ))}
      </Cards>
    )
  }
}


export default class FestivalListContainer extends React.Component {
  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      festivals: null,
      error: null,
    }
  }

  componentDidMount() {
    const { store } = this.context
    store.findAll('festival', {})
      .then((festivals) => {
        this.setState({
          festivals,
          error: null,
        })
      })
      .catch(() => {
        this.setState({
          loading: false,
          error: 'something went wrong',
        })
      })
  }

  render() {
    const { festivals, error } = this.state
    return (
      <Page
        isLoading={!festivals && !error}
        contentError={error}
        content={
          festivals ? <FestivalList festivals={festivals} /> : ''
        }
      />
    )
  }
}
