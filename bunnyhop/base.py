import requests
import json
from .url_settings import *

class BaseBunny(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint_url = bunnycdn_url

    def get_header(self):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'AccessKey': self.api_key
        }
        return header

    def call_api(self, api_url, api_method, header, api_data={}, format=True):
        if api_method == "POST":
            r = requests.request(method=api_method, url=api_url, headers=header, json=api_data)
        else:
            r = requests.request(method=api_method, url=api_url, headers=header, params=api_data)
        
        if format:
            return self.format_response(r)
        else:
            return r

    def format_response(self, r):
        if r.status_code == 404:
            response = {
                    "status": "error",
                    "status_code": r.status_code,
                    "result": None,
                }
            return json.dumps(response)
        else:
            r_header = r.headers.get('content-type')
            if(r_header.__contains__('application/json')):
                if r.status_code == 201 or r.status_code == 200 or r.status_code == 204:
                    response = {
                        "status": "successful",
                        "status_code": r.status_code,
                        "result": r.text,
                    }
                    return json.dumps(response)
            
                else:
                    response = {
                        "status": "error",
                        "status_code": r.status_code,
                        "result": r.text,
                    }
                    return json.dumps(response)
            else:
                return "incorrect API Key"