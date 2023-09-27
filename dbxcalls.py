from az.cli import az
import json

# AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
exit_code, result_dict, logs = az("group show -n Bicep-rg")

output=az("group list")[1]

#/ On 0 (SUCCESS) print result_dict, otherwise get info from `logs`
#print (result_dict)
print(output)

#data = json.load(result_dict)
#for i in data:
#    print(i)
