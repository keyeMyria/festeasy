import React, { PropTypes } from 'react';


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
  festival: PropTypes.object.isRequired,
}


export default class FestivalContainer extends React.Component {
  constructor(props, context) {
    super(props)
    this.state = {
      loading: true,
      festival: null,
      error: null,
    }
    context.store.find('festival', this.props.params.festivalId)
      .then((festival) => {
        this.setState({
          loading: false,
          error: null,
          festival,
        })
      })
      .catch((error) => {
        this.setState({
          loading: false,
          error,
        })
      })
  }

  render() {
    const { festival, error } = this.state
    if (festival) {
      return <Festival festival={festival} />
    } else if (error) {
      return <div>Error.</div>
    } else {
      return <div>Loading...</div>
    }
  }
}

FestivalContainer.propTypes = {
  params: PropTypes.object.isRequired,
}

FestivalContainer.contextTypes = {
  store: PropTypes.object.isRequired,
}
