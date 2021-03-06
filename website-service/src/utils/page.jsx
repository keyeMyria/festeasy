import React, { PropTypes } from 'react'


export default class Page extends React.Component {
  static propTypes = {
    header: PropTypes.any,
    isLoading: PropTypes.bool,
    isRefreshing: PropTypes.bool,
    content: PropTypes.any,
    contentError: PropTypes.any,
  }

  render() {
    const {
      header,
      isLoading,
      content,
      contentError,
    } = this.props
    let result
    if (isLoading) {
      result = (
        <div className="ui active centered inline large text loader">
          Loading...
        </div>
      )
    } else if (contentError) {
      result = contentError
    } else if (content) {
      result = content
    } else {
      result = <div>No idea</div>
    }
    return (
      <div>
        {header}
        {result}
      </div>
    )
  }
}
