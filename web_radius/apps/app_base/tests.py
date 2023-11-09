#from django.test import TestCase

import requests

url = 'https://utm_ip:8443/fwrules_importer/trigger_update'

response = requests.post(url=url, verify=False)

print(response.text)