import React from 'react';
import shallowCompare from 'react-addons-shallow-compare';
import Tab from './tab.jsx'
import DefaultProps from './defaultProps.jsx';
import TabMenu from './tabmenu.jsx';
// import Tab from './tab.jsx';

export default class Tabs extends React.Component {
  static propTypes = {
    ...DefaultProps.propTypes,
        /**
         * Active tab value
         */
    activeTab: React.PropTypes.oneOfType([
      React.PropTypes.number,
      React.PropTypes.string,
    ]).isRequired,
        /**
         * Current tab want's to be changed
         */
    onTabChange: React.PropTypes.func,
  };

  static defaultProps = {
    ...DefaultProps.defaultProps,
    onTabChange: () => {},
  };

    /* eslint-disable */
    static Components = {
        TabMenu: TabMenu,
        Tab: Tab
    };
    /* eslint-enable */

  shouldComponentUpdate(nextProps, nextState) {
    return shallowCompare(this, nextProps, nextState);
  }

  onMenuChange = (value) => {
    const { onTabChange, activeTab } = this.props;
    if (value && value !== activeTab) {
      onTabChange(value);
    }
  }

  renderMenu() {
    const { activeTab } = this.props;
        // Menu should be first element
    const children = React.Children.toArray(this.props.children).shift();
    if (children && children.type === Tabs.Components.TabMenu) {
      return React.cloneElement(children, {
        menuValue: activeTab,
        onMenuChange: this.onMenuChange,
      });
    }
    return null;
  }

  renderTabs() {
    const { children, activeTab } = this.props;
    const childrenWithoutMenu = React.Children.toArray(children);
    childrenWithoutMenu.shift();
    console.log('children tabs: ', childrenWithoutMenu)
    return childrenWithoutMenu.map(child => {
      if (!child || child.type !== Tabs.Components.Tab) {
        return null;
      }

      return React.cloneElement(child, {
        key: child.key ? child.key : child.props.value,
        active: child.props.value === activeTab,
      });
    })
  }

  render() {
    const { component, defaultClasses, children, activeTab, onTabChange, ...other } = this.props;
    const Component = component;

    return (
      <Component {...other}>
				{this.renderMenu()}
				{this.renderTabs()}
      </Component>
        );
  }
}
