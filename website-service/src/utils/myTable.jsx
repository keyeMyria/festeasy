import React, { PropTypes } from 'react'
import { Table, Tr, Td } from 'semantic-react'


class MyTh extends React.Component {
  render() {
    return (
      <th {...this.props} />
    )
  }
}


class MyTd extends React.Component {
  render() {
    return (
      <Td {...this.props} />
    )
  }
}


class MyTr extends React.Component {
  render() {
    return (
      <Tr {...this.props} />
    )
  }
}


class MyTable extends React.Component {
  static propTypes = {
    headers: PropTypes.object,
    rows: PropTypes.array,
  }

  render() {
    return (
      <Table {...this.props}>
        <thead>
          {this.props.headers}
        </thead>
        <tbody>
          {this.props.rows}
        </tbody>
      </Table>
    )
  }
}

module.exports = { MyTable, MyTr, MyTd, MyTh }
