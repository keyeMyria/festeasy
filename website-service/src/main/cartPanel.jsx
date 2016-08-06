import React, { Component, PropTypes } from 'react';
import { MenuItem, Tabs, TabMenu } from 'semantic-react'
import CartItem from './cartItem.jsx'

export default class CartPanel extends Component {
  // static propTypes = {
  // }
  constructor(props) {
    super(props);
    this.state = {
      active: 1,
    }
  }
  render() {
    return (
      <Tabs onTabChange={(val) => this.setState({ active: val })} activeTab={this.state.active}>
        <TabMenu vertical >
          <MenuItem menuValue={1}>
          hi
          </MenuItem>
          <MenuItem menuValue={2}>second</MenuItem>
          <MenuItem menuValue={3}>Third</MenuItem>
          <MenuItem menuValue={4}>Four</MenuItem>
        </TabMenu>

      </Tabs>
    )
  }
}
