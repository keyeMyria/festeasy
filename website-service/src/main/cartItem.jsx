import React, { PropTypes } from 'react';

export default class CartItem extends React.Component {
  render() {
    return (
      <div>
        <div className="ui items">
          <div className="item">
            <div className="ui tiny image">
              <img src="/images/beer.png" role="presentation" />
            </div>
            <div className="content">
              <a className="header">Beer</a>
              <div className="meta">
                <span>Golden Liquid Lunch</span>
              </div>
              <div className="description">
                <p>5</p>
              </div>
              <div className="extra">
                Have a jolly good time in the sun
              </div>
            </div>
          </div>
        </div>
        <div className="ui divider" />
      </div>
    )
  }
}
