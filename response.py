LIST1={'id': '/subscriptions/e012207b-8e1b-4f26-8a4f-ca977909d894/resourceGroups/DBX-RG/providers/Microsoft.Databricks/workspaces/DBX-DEVOPS-WORKSPACE1', 'location': 'eastus', 'name': 'DBX-DEVOPS-WORKSPACE1', 'authorizations': [{'principalId': '9a74af6f-d153-4348-988a-e2672920bee9', 'roleDefinitionId': '8e3af657-a8ff-443c-a75c-2fe8c4bcb635'}], 'createdBy': {'applicationId': '04b07795-8ddb-461a-bbee-02f9e1bf7b46', 'oid': '97365781-a52d-4384-a8ad-b7c4409ec56d', 'puid': '10033FFFA9EC714B'}, 'createdDateTime': '2023-09-29T20:31:06.942162Z', 'managedResourceGroupId': '/subscriptions/e012207b-8e1b-4f26-8a4f-ca977909d894/resourceGroups/databricks-rg-DBX-DEVOPS-WORKSPACE1-lcm6c3j2liy9a', 'parameters': {'enableNoPublicIp': {'type': 'Bool', 'value': False}, 'natGatewayName': {'type': 'String', 'value': 'nat-gateway'}, 'prepareEncryption': {'type': 'Bool', 'value': False}, 'publicIpName': {'type': 'String', 'value': 'nat-gw-public-ip'}, 'requireInfrastructureEncryption': {'type': 'Bool', 'value': False}, 'resourceTags': {'type': 'Object'}, 'storageAccountName': {'type': 'String', 'value': 'dbstorager3iwpgwo4cwoy'}, 'storageAccountSkuName': {'type': 'String', 'value': 'Standard_GRS'}, 'vnetAddressPrefix': {'type': 'String', 'value': '10.139'}}, 'provisioningState': 'Succeeded', 'updatedBy': {'applicationId': '04b07795-8ddb-461a-bbee-02f9e1bf7b46', 'oid': '97365781-a52d-4384-a8ad-b7c4409ec56d', 'puid': '10033FFFA9EC714B'}, 'workspaceId': '3158278331711109', 'workspaceUrl': 'adb-3158278331711109.9.azuredatabricks.net', 'sku': {'name': 'Standard'}, 'type': 'Microsoft.Databricks/workspaces', 'resourceGroup': 'DBX-RG'}
print(LIST1['id'])
print(LIST1['workspaceUrl'])