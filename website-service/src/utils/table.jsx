import React, { PropTypes, Component } from 'react'
import { Table, Tr, Td } from 'semantic-react'


class BasicTable extends Component {
  static propTypes = {
    headers: PropTypes.array.isRequired,
    rows: PropTypes.array.isRequired,
    onRowClick: PropTypes.func,
    componentProps: PropTypes.object,
  }

  handleRowClick = r => {
    if (this.props.onRowClick) {
      this.props.onRowClick(r)
    }
  }

  render() {
    const { headers, rows, componentProps } = this.props
    const rowStyle = {}
    if (this.props.onRowClick) {
      rowStyle.cursor = 'pointer'
    }
    return (
      <Table
        {...componentProps}
      >
        <thead>
          <Tr>
            {headers.map((h) => (
              <th key={h.attr}>{h.label}</th>
            ))}
          </Tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <Tr
              style={rowStyle}
              key={r.id}
              onClick={() => this.handleRowClick(r)}
            >
              {headers.map((h) => (
                <Td key={h.attr}>{r[h.attr]}</Td>
              ))}
            </Tr>
          ))}
        </tbody>
      </Table>
    )
  }
}

module.exports = {
  BasicTable,
}
