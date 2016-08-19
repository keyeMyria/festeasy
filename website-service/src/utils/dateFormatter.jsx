import React, { PropTypes } from 'react'
import moment from 'moment'


export default function DateFormatter(props) {
  return <span>{moment(props.date).format('LLLL')}</span>
}

DateFormatter.propTypes = {
  date: PropTypes.string.isRequired,
}
