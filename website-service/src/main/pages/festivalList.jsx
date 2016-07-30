import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { festivalShape } from 'utils/shapes.jsx'
import Page from 'common/page.jsx'
import DateFormatter from 'utils/dateFormatter.jsx'


class FestivalListItem extends React.Component {
  static propTypes = {
    festival: festivalShape.isRequired,
  }

  render() {
    const festival = this.props.festival
    return (
      <div>
        <h2>
          <Link to={`/festivals/${festival.id}`}>
            {festival.name}
          </Link>
        </h2>
        <p>{festival.description}</p>
        <p>Starts: <DateFormatter date={festival.starts_on} /></p>
      </div>
    )
  }
}


class FestivalList extends React.Component {
  static propTypes = {
    festivals: PropTypes.arrayOf(
      festivalShape
    ).isRequired,
  }

  render() {
    const { festivals } = this.props
    return (
      <div>
        {festivals.map(festival => (
          <div key={festival.id}>
            <FestivalListItem festival={festival} />
            <div className="ui divider" />
          </div>
        ))}
      </div>
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

  componentWillMount() {
    const { store } = this.context
    store.findAll('festival', {}, { bypassCache: true })
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
