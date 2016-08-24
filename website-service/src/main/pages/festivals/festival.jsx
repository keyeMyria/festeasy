import React, { PropTypes } from 'react';
import { Link } from 'react-router'
import { Grid, Column, Image, Header, Breadcrumb, Divider } from 'semantic-react'
import Page from 'utils/page.jsx'
import DateFormatter from 'utils/dateFormatter.jsx'
import SelectFestivalButton from 'main/components/selectFestivalButton.jsx'
import apiEndpoint from 'apiEndpoint.js'


class Festival extends React.Component {
  static propTypes = {
    festival: PropTypes.object.isRequired,
  }

  render() {
    const { festival } = this.props
    const imageHeight = 250
    return (
      <div>
        <Breadcrumb>
          <Link className="section" to="/festivals">All Festivals</Link>
          <i className="right angle icon divider" />
          <Link className="section" to={`/festivals/${festival.id}`}>
            {festival.name}
          </Link>
        </Breadcrumb>
        <br />
        <br />
        <Grid columns={2}>
          <Column width={6}>
            {festival.image_id ?
              <Image
                centered
                style={{ maxHeight: imageHeight, width: 'auto', height: 'auto' }}
                alt="product thumbnail"
                src={apiEndpoint.concat(
                  `v1/images/${festival.image_id}/image?height=${imageHeight}`
                )}
              /> : 'No thumbnail image'
            }
          </Column>
          <Column>
            <Header>{festival.name}</Header>
            <p>{festival.description}</p>
            <p>Starts On: <DateFormatter date={festival.starts_on} /></p>
            <SelectFestivalButton festival={festival} />
          </Column>
        </Grid>
        <Divider />
      </div>
    )
  }
}


export default class FestivalContainer extends React.Component {
  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      festival: null,
      error: null,
    }
  }

  componentDidMount() {
    const { store } = this.context
    const { festivalId } = this.props.params
    store.find('festival', festivalId)
      .then((festival) => {
        this.setState({
          festival,
          error: null,
        })
      })
      .catch(() => {
        this.setState({
          loading: false,
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { festival, error } = this.state
    return (
      <Page
        isLoading={!festival && !error}
        contentError={error}
        content={
          festival ? <Festival festival={festival} /> : ''
        }
      />
    )
  }
}
