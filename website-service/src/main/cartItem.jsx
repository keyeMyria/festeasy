import React, { PropTypes } from 'react';

export default class CartItem extends React.Component {
  render() {
    return (
      <div>
        <div className="ui header">
          <div className="ui four column grid">
            <div className="row">
              <div className="column">hi</div>
              <div className="column">there</div>
              <div className="column">this</div>
            </div>
            <div className="column">is</div>
            <div className="column">cool</div>
            <div className="column">and</div>
            <div className="column">stuff</div>
          </div>
        </div>
        <div className="ui header">
          this is an image of the thing
        </div>
      </div>
    )
  }
}
