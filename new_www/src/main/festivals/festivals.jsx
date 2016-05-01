import React, { PropTypes } from 'react'
import { Link } from 'react-router';
import { connect } from 'react-redux'


const festivalShape = PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    starts_on: PropTypes.string.isRequired,
    ends_on: PropTypes.string.isRequired,
})


const FestivalListItem = ({ festival }) => (
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


FestivalListItem.propTypes = {
  festival : festivalShape
}


const FestivalList = React.createClass({
  propTypes: {
    festivals : PropTypes.arrayOf(
      festivalShape
    ),
    isFetching: PropTypes.bool
  },


  render: function() {
    return (
      <div>
        <h1>Festivals</h1>
        {this.props.festivals.map(festival =>
          <div key={festival.id}>
            <FestivalListItem festival={festival}/>
          </div>
        )}
      </div>
    )
  }
})


const mapStateToProps = state => ({
  festivals: state.festivals.items || [],
  isFetching: state.festivals.isFetching
})


const FestivalsContainer = connect(mapStateToProps)(FestivalList)


module.exports = FestivalsContainer
