import React, { PropTypes } from 'react'
import { Grid, Column, Menu, Segment } from 'semantic-react'
import NavLink from 'common/navLink.jsx'


export default class Account extends React.Component {
  static propTypes = {
    children: PropTypes.any,
  }

  render() {
    return (
      <div className="ui container">
        <Grid columns={2}>
          <Column width={4}>
            <Menu vertical pointing>
              <NavLink to="/account/orders">Orders</NavLink>
              <NavLink to="/account/settings">Settings</NavLink>
            </Menu>
          </Column>
          <Column width={12}>
            <Segment>
              {this.props.children}
            </Segment>
          </Column>
        </Grid>
      </div>
    )
  }
}
