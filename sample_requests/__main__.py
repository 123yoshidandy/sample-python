# coding: utf-8

import requests


response = requests.get('http://google.com')
print(response.status_code)
print(response.text)
