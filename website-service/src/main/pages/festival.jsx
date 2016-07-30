import React, { PropTypes } from 'react';
import Page from 'common/page.jsx'


class Festival extends React.Component {
  static propTypes = {
    festival: PropTypes.object.isRequired,
  }

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


export default class FestivalContainer extends React.Component {
  static propTypes = {
    params: PropTypes.object.isRequired,
  }

  static contextTypes = {
    store: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      festival: null,
      error: null,
    }
  }

  componentWillMount() {
    const { store } = this.context
    const { festivalId } = this.props.params
    store.find('festival', festivalId)
      .then((festival) => {
        this.setState({
          festival,
          error: null,
        })
      })
      .catch(() => {
        this.setState({
          loading: false,
          error: 'Something went wrong',
        })
      })
  }

  render() {
    const { festival, error } = this.state
    return (
      <Page
        isLoading={!festival && !error}
        contentError={error}
        content={
          festival ? <Festival festival={festival} /> : ''
        }
      />
    )
  }
}
