import requests
import json

def solver(**kwargs):

    endpoint = "http://{kwargs.get('geoloc')}.api.decisionrules.io/rule/solve/" if ('geoloc' in kwargs) else 'http://api.decisionrules.io/rule/solve/'

    if 'version' in kwargs:
        endpoint += f"{kwargs.get('ruleId')}/{kwargs.get('version')}"
    else:
         endpoint += f"{kwargs.get('ruleId')}"

    header = {"Authorization": f"Bearer {kwargs.get('token')}"}

    response = requests.post(url=endpoint, json=kwargs.get('body'), headers=header)

    return response.json()
