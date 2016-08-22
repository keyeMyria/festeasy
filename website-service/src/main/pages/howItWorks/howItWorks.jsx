import React from 'react'


export default class HowItWorks extends React.Component {
  render() {
    const steps = [
      {
        name: 'Select festival and products',
      },
      {
        name: 'Checkout and Pay',
      },
      {
        name: 'Recive order and enjoy the festival',
      },
    ]
    return (
      <div className="ui container">
        <div className="ui fluid ordered steps">
          {steps.map((s) => (
            <div key={s.name} className="step">
              <div className="content">
                <div className="title">{s.name}</div>
                <div className="description">{s.description}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    )
  }
}
