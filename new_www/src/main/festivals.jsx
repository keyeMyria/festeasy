import React, { PropTypes } from 'react'
import { Link } from 'react-router';


const FestivalListItem = ({ festivalData }) => (
  <div>
    <h2>
      <Link to={`/festivals/${festivalData.id}`}>
        {festivalData.name}
      </Link>
    </h2>
    <p>{festivalData.description}</p>
    <p>Starts: {festivalData.starts_on}</p>
    <p>Ends: {festivalData.ends_on}</p>
  </div>
)


FestivalListItem.propTypes = {
  festivalData : PropTypes.object.isRequired
}


const FestivalList = ({ festivals }) => (
  <div>
    <h1>Festivals</h1>
    {festivals.map(festival =>
      <div key={festival.id}>
        <FestivalListItem festivalData={festival}/>
      </div>
    )}
  </div>
)


FestivalList.propTypes = {
  festivals: PropTypes.array.isRequired
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
