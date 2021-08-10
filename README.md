# DecisionRulespy

Simple async python library that allows you to easily connect to [Decisionrules.io](https://decisionrules.io) from your python application.

# Where do I get api key?

You can create your API key here: https://app.decisionrules.io/api-keys

# Init arguments

* apiKey - apikey (string)
* GeoLocation - enum of possible [geoLocations](https://docs.decisionrules.io/docs/api/geo-location) (optional argument)
* CustomDomain - if you have on-premise solution you can inject your own server domain name and transfer protocol with this class (if normal DR are used you can omit this)

# Arguments

* ruleId - id of the rule from dashboard (string)
* data - request object. Omit data object. f.e {data:{myreq: something}} - WRONG, {myreq: something} - GOOD 
* SolverStrategy - enum of possible [solver strategies](https://docs.decisionrules.io/docs/other/execution-strategy)
* version - version of the rule. optional argument

If you omit version then you will automaticaly get result of your latest version deployed on DecisionRules dashboard.

If you omit geo location your request will be computed on default server in Europe.

We offer these geoLocs:

- eu1: Ireland
- eu2: Sweden
- us1: Virginia
- us2: North California

# Simple usage demo

````python
import decisionrules
import asyncio

apikey = "API_KEY_HERE"
geoLoc = decisionrules.GeoLocations.US2
solver_strategy = decisionrules.SolverStrategies.STANDARD

decisionrules.init(apikey, geoLoc)

data = {"day": "today"}


async def get_result(request):
    result = await decisionrules.solver("RULE_ID_HERE", request, solver_strategy)
    print(result[0]["result"])


loop = asyncio.get_event_loop()

loop.run_until_complete(get_result(data))
````

## Custom domain usage

Just create CustomDomain instance that takes string url and Protocols enum value as params and pass to the init function.

```python
customDomain = decisionrules.CustomDomain("your.domain.com", decisionrules.Protocols.HTTPS)

decisionrules.init(apikey, geoLoc, customDomain)
```

# Dependencies

[Requests](https://pypi.org/project/requests/)
