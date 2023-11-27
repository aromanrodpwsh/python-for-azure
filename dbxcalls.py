from az.cli import az
import json
rgname = 'Bicep-rg'
# AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
exit_code, result_dict, logs = az("group show -n '{rgname}'")

output=az("group list")[1][0]
if 'eastus' in output['location']:
    print (output['name'])
