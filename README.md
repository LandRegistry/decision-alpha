#decision

Eventually this wants replacing with something like cucumber tests, 
but for now it is just a few simple functions that return some codes.

Multiple codes can be returned, up to the client to decide what to do with them.

Return codes look like:

{
  "decision":[
    {"code": 100},
  ]
}

## Codes

### 1xx - casework

100 - send to casework

### 2xx - check list

200 - send for checking

TODO:

Probably needs some kind of signing of the response, maybe a verifiable hash of the data/decision?