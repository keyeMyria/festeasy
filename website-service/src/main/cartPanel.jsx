import React from 'react';
import { MenuItem } from 'semantic-react'
// import { Tab } from 'semantic-react'
import Tabs from '../components/sidePanel/tabs.jsx'
import TabMenu from '../components/sidePanel/tabmenu.jsx'
import Tab from '../components/sidePanel/tab.jsx'

// import CartItem from './cartItem.jsx'


export default class CartPanel extends React.Component {
  // static propTypes = {
  // }
  constructor(props) {
    super(props);
    this.state = {
      active: 2,
    }
  }
  render() {
    return (
      <div>
        <Tabs onTabChange={(val) => this.setState({ active: val })} activeTab={this.state.active}>
          <TabMenu vertical >
            <MenuItem menuValue={2}>second<Tab value={2}>second</Tab></MenuItem>
            <MenuItem menuValue={3}>Third</MenuItem>
            <MenuItem menuValue={4}>Four</MenuItem>
          </TabMenu>
          <Tab value={3}>something else here</Tab>
        </Tabs>
        <div>
          {this.state.active}
        </div>
      </div>
    )
  }
}
