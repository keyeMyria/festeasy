import React, { PropTypes } from 'react';

export default class CartItem extends React.Component {
  render() {
    return (
      <div>
        <div className="ui feed">
          <div className="event">
            <div className="label">
              <img src="/images/avatar/small/elliot.jpg" role="presentation" />
            </div>
            <div className="content">
              You bought this stuff <a>Beers</a>
            </div>
          </div>
        </div>
        <div className="ui divider" />
      </div>
    )
  }
}
