import React, { PropTypes, Component } from 'react'
import { Table, Tr, Td } from 'semantic-react'


const PaginationMenu = ({ currentPageNumber, totalPages, onPageChange, colSpan }) => {
  const cp = newPageNumber => {
    if (newPageNumber <= totalPages && newPageNumber > 0) {
      onPageChange(newPageNumber)
    }
  }

  return (
    <Tr>
      <th colSpan={colSpan}>
        <div className="ui right floated pagination menu">
          <a
            className={'icon item '.concat(currentPageNumber <= 1 ? 'disabled' : '')}
            onClick={() => cp(currentPageNumber - 1)}
          >
            <i className="left chevron icon" />
          </a>
          <div className="item">
            Page {currentPageNumber} of {totalPages}
          </div>
          <a
            className={'icon item '.concat(currentPageNumber >= totalPages ? 'disabled' : '')}
            onClick={() => cp(currentPageNumber + 1)}
          >
            <i className="right chevron icon" />
          </a>
        </div>
      </th>
    </Tr>
  )
}

PaginationMenu.propTypes = {
  currentPageNumber: PropTypes.number.isRequired,
  totalPages: PropTypes.number.isRequired,
  onPageChange: PropTypes.func.isRequired,
  colSpan: PropTypes.number.isRequired,
}


class BasicTable extends Component {
  static propTypes = {
    headers: PropTypes.array.isRequired,
    rows: PropTypes.array.isRequired,
    onRowClick: PropTypes.func,
    componentProps: PropTypes.object,
    paginationInfo: PropTypes.object,
  }

  handleRowClick = r => {
    if (this.props.onRowClick) {
      this.props.onRowClick(r)
    }
  }

  paginationMenu = () => {
    if (this.props.paginationInfo) {
      const { totalPages, currentPageNumber, onPageChange } = this.props.paginationInfo
      return (
        <PaginationMenu
          totalPages={totalPages}
          currentPageNumber={currentPageNumber}
          onPageChange={onPageChange}
          colSpan={this.props.headers.length}
        />
      )
    }
    return null
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
          {this.paginationMenu()}
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
                <Td key={h.attr}>
                  {h.cellComponent ?
                    React.createElement(h.cellComponent, { value: r[h.attr] })
                  : r[h.attr]}
                </Td>
              ))}
            </Tr>
          ))}
        </tbody>
        <tfoot>{this.paginationMenu()}</tfoot>
      </Table>
    )
  }
}

module.exports = {
  BasicTable,
}
