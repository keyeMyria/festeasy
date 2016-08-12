/**
 * Default prop types
 */

import React from 'react';
import elementType from 'react-prop-types/lib/elementType';

/**
 * Need component to pass into react-docgen
 */
const DefaultProps = () => (
  <noscript />
)

DefaultProps.propTypes = {
  /**
   * Children nodes
   */
  children: React.PropTypes.node,
  /**
   * Use other component for composing results: <DropdownMenu component={Button}>
   */
  component: elementType,
  /**
   * Apply default semantic UI classes for component, for example ui button
   */
  defaultClasses: React.PropTypes.bool,
  /**
   * Additional CSS ui classes
   */
  className: React.PropTypes.string,
};

DefaultProps.defaultProps = {
  component: 'div',
  defaultClasses: true,
};

export default DefaultProps;
