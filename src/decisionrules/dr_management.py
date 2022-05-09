import requests

from .custom_domain import *
from .exceptions import *

class ManagementApi():

    _management_api: str
    _custom_domain: CustomDomain

    _header: dict
    

    def __init__(self, management_api_key, custom_domain: CustomDomain = None):
        global _management_api
        _management_api = management_api_key
        global _custom_domain
        _custom_domain = custom_domain
        global _header
        _header = self.header_factory(_management_api)


    def header_factory(self, api_key):
        return {"Authorization": f"Bearer {api_key}"}


    def url_factory(self):
        if _custom_domain is not None:
            return f"{_custom_domain.custom_domain_protocol.value}://{_custom_domain.custom_domain_url}/api"
        else:
            return "https://api.decisionrules.io/api"


    async def get_call(self, get_url):
        response = None


        response = await requests.get(get_url, headers=_header)

        return response.json()
        

    async def get_rule(self, rule_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule/{rule_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule/{rule_id}"

        return await self.get_call(url)



    async def get_space(self, space_id):
        url = f"{self.url_factory()}/space/{space_id}"

        return await self.get_call(url)



    async def create_rule(self, space_id, data):
        url = f"{self.url_factory()}/rule/{space_id}"

        response = None

        
        response = await requests.post(url, json=data, headers=_header)
        return response.json()


    async def update_rule(self, rule_id, version, data):
        url = f"{self.url_factory()}/rule/{rule_id}/{version}"

        response = None

        
        response = await requests.put(url, json=data, headers=_header)
        return
        

    async def delete_rule(self, rule_id, version):
        url = f"{self.url_factory()}/rule/{rule_id}/{version}"

        response = None

        await requests.delete(url, headers=_header)
        return


    async def get_ruleflow(self, ruleflow_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}"

        print(url)

        return await self.get_call(url)


    async def create_ruleflow(self, data):
        url = f"{self.url_factory()}/rule-flow/"

        response = None

        response = await  requests.post(url,json=data, headers=_header)
        return response.json()


    async def update_ruleflow(self, ruleflow_id, version, data):
        url = f"{self.url_factory()}/rule-flow/{ruleflow_id}/{version}"

        response = None

        response = await requests.put(url, json=data, headers=_header)
        return


    async def delele_ruleflow(self, ruleflow_id, version = None):
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}"
        

        response = None

        await requests.delete(url, headers=_header)
        return


    async def export_ruleflow(self, ruleflow_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}"

        return await self.get_call(url)


    async def import_ruleflow(self, data, ruleflow_id = None, current_version = None):
        url = None
        if ruleflow_id is None and current_version is None:
            url = f"{self.url_factory()}/rule-flow/import"
        elif ruleflow_id is not None:
            url = f"{self.url_factory()}/rule-flow/import/?new-version={ruleflow_id}"
        elif ruleflow_id is not None and current_version is not None:
            url = f"{self.url_factory()}/rule-flow/import/?overwrite={ruleflow_id}&version={current_version}"

        response = None

        response = await requests.post(url=url, json=data, headers=_header)

        return response.json()


    async def change_rule_status(self, ruleId, status, version):
        url = f"{self.url_factory()}/rule/status/{ruleId}/{status}/{version}"

        response = await requests.put(url=url, headers=_header)

        return response.json()

    async def getItems(self, tags):

        tagsQuery = ",".join(map(str, tags))

        url = f"{self.url_factory()}/tags/items/?tags={tagsQuery}"

        response = await requests.get(url)

        return response.json()

    async def updateTags(self, ruleId, data, version=None):
        
        url = ""

        if version is not None:
            url = f"{self.url_factory()}/tags/{ruleId}"
        else:
            url = f"{self.url_factory()}/tags/{ruleId}/{version}"

        response = await requests.patch(url, data=data)

        return response.json()

    async def deleteTags(self, ruleId, version=None):

        url = ""

        if version is not None:
            url = f"{self.url_factory()}/tags/{ruleId}"
        else:
            url = f"{self.url_factory()}/tags/{ruleId}/{version}"

        await requests.delete(url)

        return