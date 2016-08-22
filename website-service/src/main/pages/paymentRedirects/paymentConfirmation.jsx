import React from 'react'
import { Header, Container, Grid, Column } from 'semantic-react'


export default class PaymentConfirmation extends React.Component {
  render() {
    return (
      <Container>
        <Header aligned="center">Payment Confirmed</Header>
        <Grid aligned="center">
          <Column>
            <p>
              Yay! Thank you for using FestEasy!
            </p>
            <p>
              We have emailed you your payment receit.
            </p>
            <p>
              Please print this receit
              and present it when collecting your order from FestEasy.
            </p>
            <p>
              If you have any queries, please contact&nbsp;
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
