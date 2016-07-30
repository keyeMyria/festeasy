import React from 'react';
import Page from 'common/page.jsx'


const About = () => (
  <Page
    header={
      <h2 className="ui header">About</h2>
    }
    content={
      'Some about content here'
    }
  />
)

module.exports = About
