import React, { PropTypes } from 'react';
import { connect, PromiseState } from 'react-refetch'


const Festival = React.createClass({
  propTypes: {
    festival: PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired
    })
  },


  render: function() {
    const { festival } = this.props
    return (
      <div>
        <h1>{festival.name}</h1>
        <p>{festival.description}</p>
        <p>Starts On: {festival.starts_on}</p>
        <p>Ends On: {festival.ends_on}</p>
      </div>
    )
  }
})


const FestivalContainer = React.createClass({
  render: function() {
    const { festivalFetch } = this.props
    if (festivalFetch.pending) {
      return <div>Loading...</div>
    } else if (festivalFetch.rejected) {
      return <div>Error</div>
    } else if (festivalFetch.fulfilled) {
      return <Festival festival={festivalFetch.value}/>
    }
  }
})


export default connect(function(props) {
  return {
    festivalFetch: `http://localhost:5000/api/v1/festivals/${props.params.festivalId}`
  }
})(FestivalContainer)
