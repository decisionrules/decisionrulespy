import requests
import json

def solver(ruleId, body, token, geoloc="eu1", version=""):

    if(ruleId != None or ruleId == ""):
        raise Exception("RuleID is mandatory argument")

    if(body != None or body == ""):
        raise Exception("Body is mandatory argument")

    if(token != None or token == ""):
        raise Exception("API Token is mandatory argument")

    endpoint = ""

    if(version != ""):
        endpoint = f"http://{geoloc}.api.decisionrules.io/rule/solve/{ruleId}/{version}"

    endpoint = f"http://{geoloc}.api.decisionrules.io/rule/solve/{ruleId}"

    header = {"Authorization": f"Bearer {token}"}

    response = requests.post(url=endpoint, json=body, headers=header)

    return response.json()
