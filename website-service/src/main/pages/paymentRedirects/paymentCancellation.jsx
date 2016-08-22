import React from 'react'
import { Link } from 'react-router'
import { Header, Container, Grid, Column } from 'semantic-react'


export default class PaymentCancellation extends React.Component {
  render() {
    return (
      <Container>
        <Header aligned="center">Payment Cancelled</Header>
        <Grid aligned="center">
          <Column>
            <p>
              Hello! It looks like your payment was cancelled.
            </p>
            <p>
              If you would like to re-try your payment, please go to&nbsp;
              <Link to="/account/orders">
                your orders page
              </Link>
            </p>
            <p>
              If you are having any trouble at all, please contact&nbsp;
              <a
                href="mailto:admin@festeasy.co.za"
              >
                admin@festeasy.co.za
              </a>
            </p>
          </Column>
        </Grid>
      </Container>
    )
  }
}
