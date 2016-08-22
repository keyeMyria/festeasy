import React, { PropTypes } from 'react'


export default function PriceFormatter(props) {
  return <span>R{props.rands.toFixed(2)}</span>
}

PriceFormatter.propTypes = {
  rands: PropTypes.number.isRequired,
}
