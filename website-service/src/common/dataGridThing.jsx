import React, { PropTypes, Component } from 'react'
import { BasicTable } from 'utils/table.jsx'
import { Loader } from 'utils/loader.jsx'
import { Error } from 'utils/error.jsx'


export default class DataGridThing extends Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }

  static propTypes = {
    fetchData: PropTypes.func.isRequired,
    fetchDataResponse: PropTypes.object.isRequired,
    headers: PropTypes.array.isRequired,
    onRowClick: PropTypes.func,
    queryParams: PropTypes.object.isRequired,
    onQueryPramsChange: PropTypes.func,
  }

  componentDidMount() {
    this.props.fetchData(this.props.queryParams)
  }

  componentDidUpdate(prevProps) {
    if (prevProps.queryParams !== this.props.queryParams) {
      this.props.fetchData(this.props.queryParams)
    }
  }

  render() {
    let result = <Loader />
    const { queryParams, headers, fetchDataResponse, onRowClick, onQueryPramsChange } = this.props
    const { errors, data, meta } = fetchDataResponse
    if (errors) {
      result = <Error />
    } else if (data) {
      result = (
        <BasicTable
          componentProps={{ selectable: true }}
          onRowClick={onRowClick ? r => onRowClick(r) : null}
          headers={headers}
          rows={data}
          // TODO: Improve.
          paginationInfo={{
            onPageChange: pageNumber => onQueryPramsChange({ 'page-number': pageNumber }),
            totalPages: meta.total_pages,
            currentPageNumber: parseInt(queryParams['page-number'], 10) || 1,
          }}
        />
      )
    }
    return result
  }
}
