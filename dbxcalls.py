from az.cli import az
import json

# AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
exit_code, result_dict, logs = az("group show -n Bicep-rg")

output=az("group list")[1][0]
if 'eastus' in output['location']:
    print (output['name'])