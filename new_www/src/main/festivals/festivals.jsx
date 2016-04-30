import React, { PropTypes } from 'react'
import { Link } from 'react-router';


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


const FestivalList = ({ festivals }) => (
  <div>
    <h1>Festivals</h1>
    {festivals.map(festival =>
      <div key={festival.id}>
        <FestivalListItem festival={festival}/>
      </div>
    )}
  </div>
)


FestivalList.propTypes = {
  festivals : PropTypes.arrayOf(
    festivalShape
  )
}


const FestivalsContainer = React.createClass({
  getInitialState: function() {
    return {
      festivals: []
    };
  },


  componentDidMount: function() {
    this.serverRequest = $.get('http://localhost:5000/api/v1/festivals', function(result) {
      this.setState({
        festivals: result
      })
    }.bind(this))
  },


  componentWillUnmount: function() {
    this.serverRequest.abort();
  },


  render: function() {
    return (
      <FestivalList festivals={this.state.festivals} />
    )
  }
})


module.exports = FestivalsContainer
