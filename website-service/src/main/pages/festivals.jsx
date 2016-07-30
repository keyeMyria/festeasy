import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { festivalShape } from '../../utils/shapes.jsx'


class FestivalListItem extends React.Component {
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

FestivalListItem.propTypes = {
  festival: festivalShape.isRequired,
}


class FestivalList extends React.Component {
  render() {
    const { festivals } = this.props
    return (
      <div>
        <h1>Festivals</h1>
          {festivals.map(festival => (
            <FestivalListItem key={festival.id} festival={festival} />
          ))}
      </div>
    )
  }
}

FestivalList.propTypes = {
  festivals: PropTypes.arrayOf(
    festivalShape
  ).isRequired,
}


export default class FestivalListContainer extends React.Component {
  constructor(props, context) {
    super(props)
    this.state = {
      loading: true,
      festivals: [],
      error: null,
    }
    context.store.findAll('festival')
      .then((festivals) => {
        this.setState({
          loading: false,
          error: null,
          festivals,
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
    return (
      <FestivalList festivals={this.state.festivals} />
    )
  }
}

FestivalListContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}
