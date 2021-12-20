# DecisionRulesPy

A simple library that allows you to easily connect to 
[DecisionRules.io](https://decisionrules.io) from your application.

# Usage

* Solver (Rules, Compositions)
* Management API

# 1 - Solver

Solver is designed for solving rules made in DecisionRules application.
You can run solver with `decisionrules.solver()` method. Rule ids are accessible in DecisionRules app.

## 1.1 - Defining solver init

Solver need some data beforehand, like api keys

```python
from decisionrules import *

async def solver_test():
    decisionrules.init(api_key)
```

## 1.2 - Defining solver method with data

Solver method expects 5 arguments

* SolverType - enum value - mandatory
* RuleId - str - mandatory
* Data - dict or json str - mandatory
* SolverStrategy - enum value - mandatory
* Version - str - optional

```python
async def solver_test():
    data = {"say": "Hello from python"}

    decisionrules.init(api_key)
    
    # SolverType enum changes type of solver (Rule or Compostion)
    response = await decisionrules.solver(decisionrules.SolverType.RULE, get_rule, data, SolverStrategies.STANDARD)

    response2 = await decisionrules.solver(decisionrules.SolverType.RULEFLOW, compo_rule, data, SolverStrategies.STANDARD)
```

## 1.3 Solver with custom domain

For using custom domain just add `CustomDomain` instance to the `init method` with `url` and `protocol` parameters.

```python
async def solver_test():
    data = {"say": "Hello from python"}

    decisionrules.init(api_key, CustomDomain("YOUR_URL", Protocols.HTTPS))
    
    response = await decisionrules.solver(decisionrules.SolverType.RULE, get_rule, data, SolverStrategies.STANDARD)

    response2 = await decisionrules.solver(decisionrules.SolverType.COMPOSITION, compo_rule, data, SolverStrategies.STANDARD)
```

# 2 - Management API

Management api is accessible via `dr_management` and required management api key that you can obtain in api key section in DecisionRules app.
Management api key is defined in custom `dr_management` `init` method.

```python
async def crud_test():
    dr_management.init(mng_key)
```

## 2.1 Management API usage example

```python
from decisionrules import *

async def crud_test():
    dr_management.init(mng_key)

    get_rule_resp = await dr_management.get_rule_by_id(get_rule)
    get_rule_by_version_resp = await dr_management.get_rule_by_id_and_version(get_rule, "1")
    get_space_resp = await dr_management.get_space(get_space)

    await dr_management.put_rule(put_rule, "1", put_data)
    await dr_management.post_rule(post_rule, post_data)
    await dr_management.delete_rule(delete_rule, "1")

```

## 2.3 All available methods in management API

* GetRuleById - Search for single rule by its ID
* GetRuleByIdAndVersion - Search for single rule by its ID and version
* GetSpace - Search for space by its ID
* PostRuleForSpace - Post new rule to the space
* PutRule - Update existing rule
* DeleteRule - Delete existing rule

```python
dr_management.get_rule_by_id(get_rule)

dr_management.get_rule_by_id_and_version(get_rule, "1")

dr_management.get_space(get_space)

dr_management.put_rule(put_rule, "1", put_data)

dr_management.post_rule(post_rule, post_data)

dr_management.delete_rule(delete_rule, "1")
```