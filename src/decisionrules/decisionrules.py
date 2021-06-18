import requests
from .exceptions import *

_api_key = None
_geo_location = None


def init(api_key, geo_location=None):
    global _api_key
    _api_key = api_key
    global _geo_location
    _geo_location = geo_location


def solver(rule_id, input_data, version=None):
    endpoint = url_factory(rule_id, version)

    header = {"Authorization": f"Bearer {_api_key}"}

    response = None

    try:
        response = requests.post(url=endpoint, json=input_data, headers=header)

        validate_response(response.status_code)
    except NoUserException:
        print(f"No valid user! STATUS: {response.status_code}")
        print(response.json())
    except TooManyApiCallsException:
        print(f"Too many api calls! STATUS: {response.status_code}")
        print(response.json())
    except NotPublishedException:
        print(f"Rule ain´t published yet! STATUS: {response.status_code}")
        print(response)
    except InternalServerError:
        print(f"Internal server error. STATUS: {response.status_code}")
        print(response)
    except GeneralException:
        print(f"General exception, something went wrong. STATUS: {response.status_code}")
        print(response)

    return response.json()


def url_factory(rule_id, version):
    url = None

    if _geo_location is not None:
        url = f"https://{_geo_location}.api.decisionrules.io/rule/solve/"
    else:
        url = "https://api.decisionrules.io/rule/solve/"

    if version is not None:
        url += f"{rule_id}/{version}"
    else:
        url += rule_id

    return url


def validate_response(status_code):
    if status_code == 400:
        raise NoUserException
    elif status_code == 426:
        raise TooManyApiCallsException
    elif status_code == 401:
        raise NotPublishedException
    elif status_code == 500:
        raise InternalServerError
