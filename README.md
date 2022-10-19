# Developer Advocate _API_

This project provides _API_ that shows developers information from different companies. This _API_ simply outputs the list of developers, companies they work in, list of projects they have built, and finally the skills they have.

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
