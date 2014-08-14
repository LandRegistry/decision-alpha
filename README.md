#decision

[![Build Status](https://magnum.travis-ci.com/LandRegistry/decision.svg?branch=master)](https://magnum.travis-ci.com/LandRegistry/decision)

[![Coverage Status](https://img.shields.io/coveralls/LandRegistry/decision.svg)](https://coveralls.io/r/LandRegistry/decision)


Eventually this wants replacing with something like cucumber tests, 
but for now it is just a few simple functions that return some codes.

Multiple codes can be returned, up to the client to decide what to do with them.

##Request data format
{
	"action": "change name",
	"data": {"country": "UK", "postcode":""},
	"context": {"session-id":"1234"}
}

##Response data format
Return codes look like:

{
  "decision":[
    {"code":XXX, "message":"YYY"}
  ]
}

## Codes

### 1xx - casework

100 - send to casework

### 2xx - check list

200 - send for checking

TODO:

Probably needs some kind of signing of the response, maybe a verifiable hash of the data/decision?