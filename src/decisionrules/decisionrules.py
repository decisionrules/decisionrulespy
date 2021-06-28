import requests
from .exceptions import *
from .enums import *

_api_key = None
_geo_location = None


def init(api_key, geo_location=GeoLocations.DEFAULT):
    global _api_key
    _api_key = api_key
    global _geo_location
    _geo_location = geo_location


async def solver(rule_id, input_data, solverStrategy, version=None):
    endpoint = url_factory(rule_id, version)

    header = header_factory(_api_key, solverStrategy)

    response = None

    try:
        response = requests.post(url=endpoint, json=requestParser(input_data), headers=header)

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

    if _geo_location is not GeoLocations.DEFAULT:
        url = f"http://{_geo_location.value}.api.decisionrules.io/rule/solve/"
    else:
        url = "http://api.decisionrules.io/rule/solve/"

    if version is not None:
        url += f"{rule_id}/{version}"
    else:
        url += rule_id

    print(f"sending request to: {url}")
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


def header_factory(api_key, strategy):
    if strategy is not SolverStrategies.STANDARD:
        return {"Authorization": f"Bearer {api_key}"}
    else:
        return {"Authorization": f"Bearer {api_key}", "X-Strategy": strategy.value}


def requestParser(input):
    return {
        "data": input
    }