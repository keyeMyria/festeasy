import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { connect, PromiseState } from 'react-refetch'


const festivalShape = PropTypes.shape({
  id: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  starts_on: PropTypes.string.isRequired,
  ends_on: PropTypes.string.isRequired,
})


const FestivalListItem = React.createClass({
  propTypes: {
    festival : festivalShape
  },


  render: function() {
    const festival = this.props.festival
    return(
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
})


const FestivalList = React.createClass({
  propTypes: {
    festivals : PropTypes.arrayOf(
      festivalShape
    ),
    isFetching: PropTypes.bool
  },


  render: function() {
    const { festivalsFetch } = this.props
    var festivalNodes;
    if (festivalsFetch.value) {
      festivalNodes = festivalsFetch.value.map(function(festival) {
        return <FestivalListItem key={festival.id} festival={festival} />
      })
    }
    return (
      <div>
        <h1>Festivals</h1>
        {festivalNodes}
      </div>
    )
  }
})


const FestivalsContainer = connect(props => ({
  festivalsFetch: 'http://localhost:5000/api/v1/festivals'
}))(FestivalList)


module.exports = FestivalsContainer
