import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { connect } from 'react-refetch'
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


class FestivalListContainer extends React.Component {
  render() {
    const { festivalsFetch } = this.props
    if (festivalsFetch.pending) {
      return <div>Loading...</div>
    } else if (festivalsFetch.rejected) {
      return <div>Error</div>
    } else {
      return <FestivalList festivals={festivalsFetch.value} />
    }
  }
}

FestivalListContainer.propTypes = {
  festivalsFetch: PropTypes.object.isRequired,
}


export default connect(() => ({
  festivalsFetch: 'http://localhost:5000/api/v1/festivals',
}))(FestivalListContainer)
