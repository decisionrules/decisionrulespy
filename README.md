# DecisionRulespy

Simple python library that allows you to easily connect to [Decisionrules.io](https://decisionrules.io) from your python application.

# Where do i get api key?

You can create your API key here: https://app.decisionrules.io/api-keys

# Supported kwargs

- ruleId: string
- token: string
- body: dics
- version: string
- geoloc: string

Version and Geo location are optional parameters. If you left out version then you will automaticaly get result of your latest version deployed on DecisionRules dashboard.

If you omit geo location your request will be computed on EU1 (Ireland).

We offer these values:

- eu1: Ireland
- eu2: Sweden
- us1: Virginia
- us2: North California

# Simple usage demo

````python
import decisionrulespy.decisionrules as decisionrules

ruleId="1234abcd"
token="asdf5678"
body={"data":{"my_super_input": "super_input"}}
version="1"
geoloc="eu1"

result = decisionrules.solver(ruleId=ruleId, token=token, body=body, geoloc="eu1", version="1")

````

# Dependencies

[Requests](https://pypi.org/project/requests/)
