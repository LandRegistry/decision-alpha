#decision

[![Build Status](https://magnum.travis-ci.com/LandRegistry/decision.svg?token=N9pcG7F7VybLxV2xrpVh&branch=master)](https://magnum.travis-ci.com/LandRegistry/decision)


Eventually this wants replacing with something like cucumber tests, 
but for now it is just a few simple functions that return some codes.

Multiple codes can be returned, up to the client to decide what to do with them.

##Request data format
{
	"action": "change-name-marriage",
	"data": {"iso-country-country": "GB"},
	"context": {"session-id":"1234", "transaction-id":"ABCDE"}
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
