# Developer Advocate _API_

This project provides _API_ that shows developers information from various idustries. This _API_ simply outputs the list of developers, thier company they work at, list of projects they have built, and finally the list of skills each developer has.

## Availabe Endpoints

You can access the _API_ at [developer-advocate](https://developer-advocate.herokuapp.com/) and test the following endpoints.

`/api/companies`

`/api/company/id`

`/api/advocates`

`/api/advocate/id`

`/api/projects`

The _API_ is completely searchable and has paginated.

Ex.

`/api/companies/?name=google&page=2`

`/api/advocates/?name=hadi&page=4`
