import React from 'react';
import { MyTable, MyTr, MyTd, MyTh } from 'utils/table.jsx'


export default class About extends React.Component {
  render() {
    const data = [
      {
        id: 1,
        name: 'Jason',
      },
      {
        id: 2,
        name: 'Banana',
      },
    ]
    const headers = (
      <MyTr>
        <MyTh>ID</MyTh>
        <MyTh>Name</MyTh>
      </MyTr>
    )
    const rows = data.map((thing) => (
      <MyTr key={thing.id}>
        <MyTd>{thing.id}</MyTd>
        <MyTd>{thing.name}</MyTd>
      </MyTr>
    ))
    return (
      <div>
        <h1 className="ui center aligned header">About page here</h1>
        <MyTable
          headers={headers}
          rows={rows}
        />
      </div>
    )
  }
}
