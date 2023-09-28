from azure.cli.core import get_default_cli

DBX_RG="Databricks-RG"
WORKSPACE_NAME='DBX-DEVOPS-WORKSPACE1'
DBX_LOCATION='EastUS'
DBX_SKU = 'standard'



def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True

response = az_cli("databricks workspace create --resource-group '{DBX_RG}' --name '{WORKSPACE_NAME}' --location '{DBX_LOCATION}' --sku '{DBX_SKU}'")
print(response)