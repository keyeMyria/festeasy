import React, { PropTypes } from 'react';
import { connect } from 'react-redux'


const Festival = React.createClass({
  propTypes: {
    festival: PropTypes.shape({
      id: PropTypes.number.isRequired
    })
  },


  render: function() {
    return (
      <div>
        {this.props.festival.name}
      </div>
    )
  }
})


const mapStateToProps = state => ({
  festival: state.festivals.items || {},
  isFetching: state.festivals.isFetching
})


const FestivalContainer = connect(mapStateToProps)(Festival)


module.exports = FestivalContainer
