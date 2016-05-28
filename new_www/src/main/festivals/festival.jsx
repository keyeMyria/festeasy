import React, { PropTypes } from 'react';
import { connect } from 'react-refetch'
import { festivalShape } from '../../utils/shapes.jsx'


class Festival extends React.Component {
  render() {
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
}

Festival.propTypes = {
  festival: festivalShape,
}


class FestivalContainer extends React.Component {
  render() {
    const { festivalFetch } = this.props
    if (festivalFetch.pending) {
      return <div>Loading...</div>
    } else if (festivalFetch.rejected) {
      return <div>Error</div>
    } else {
      return <Festival festival={festivalFetch.value} />
    }
  }
}

FestivalContainer.propTypes = {
  festivalFetch: PropTypes.object.isRequired,
}

export default connect((props) => ({
  festivalFetch: `http://localhost:5000/api/v1/festivals/${props.params.festivalId}`,
}))(FestivalContainer)
