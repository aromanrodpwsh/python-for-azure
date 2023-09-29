import sys
from azure.cli.core import get_default_cli

DBX_RG ="DBX-RG"
WORKSPACE_NAME = "DBX-DEVOPS-WORKSPACE1"
DBX_LOCATION = "eastus"
DBX_SKU = "Standard"


def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True

response = az_cli(f'databricks workspace create --resource-group {DBX_RG} --name {WORKSPACE_NAME} --location {DBX_LOCATION} --sku {DBX_SKU}')
print(response)

