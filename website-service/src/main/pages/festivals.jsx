import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { festivalShape } from 'utils/shapes.jsx'
import Page from 'common/page.jsx'


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
        <p>Starts: {festival.starts_on}</p>
        <p>Ends: {festival.ends_on}</p>
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
          <FestivalListItem key={festival.id} festival={festival} />
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
    store.findAll('festival')
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
        header={<h2 className="ui header">Festivals</h2>}
        isLoading={!festivals && !error}
        content={
          festivals ? <FestivalList festivals={festivals} /> : ''
        }
      />
    )
  }
}
