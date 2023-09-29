import sys
import getopt
import json
from azure.cli.core import get_default_cli

DBX_RG ="DBX-RG"
WORKSPACE_NAME = "DBX-DEVOPS-WORKSPACE1"
DBX_LOCATION = "eastus"
DBX_SKU = "Standard"
DBX_VAULT= "MainkvDbx"


def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True


def main(argv):
    try:
        global DBX_RG, WORKSPACE_NAME, DBX_LOCATION, DBX_SKU, DBX_VAULT
        USAGE_MSJ = 'createworkspace.py -w <WorkspaceName> -r <resourceGroup> -l <location> -s <sku> -v <KeyVault> '
        WORKSPACE_NAME = ''

        opts, args = getopt.getopt(argv, "hw:r:l:s:v:", [
                                   "WorkspaceName=", "resourceGroup=", "location=", "sku=", "KeyVault="])

        for opt, arg in opts:
            if opt == '-h':
                print(USAGE_MSJ)
                sys.exit(0)
            elif opt in ("-w", "--WorkspaceName"):
                if arg != '':
                    WORKSPACE_NAME = arg
                else:
                    print('Parameter <WorkspaceName> is empty')
                    sys.exit(2)
            elif opt in ("-r", "--resourceGroup"):
                if arg != '':
                    DBX_RG = arg
                else:
                    print('Parameter <resourceGroup> is empty')
                    sys.exit(2)
            elif opt in ("-l", "--location"):
                if arg != '':
                    DBX_LOCATION = arg
                else:
                    print('Parameter <location> is empty')
                    sys.exit(2)
            elif opt in ("-s", "--sku"):
                if arg != '':
                    DBX_SKU = arg
                else:
                    print('Parameter <sku> is empty')
                    sys.exit(2)
            elif opt in ("-v", "--KeyVault"):
                if arg != '':
                    DBX_VAULT = arg
                else:
                    print('Parameter <KeyVault> is empty')
                    sys.exit(2)
            else:
                print('This arg is not valid [', opt, ']')
                print(USAGE_MSJ)
                sys.exit(2)
        #dbx_response = az_cli(f'databricks workspace create --resource-group {DBX_RG} --name {WORKSPACE_NAME} --location {DBX_LOCATION} --sku {DBX_SKU}')
        #DBX_RESOURCE_ID= dbx_response['id']
        #DBX_WORKSPACE_URL=dbx_response['workspaceUrl']
        DBX_RESOURCE_ID='test cualquier cosa'
        DBX_WORKSPACE_URL='tsts otra cosa'

        print(f'Worspace successfully created with Resource Id: {DBX_RESOURCE_ID}')
        print(f'Worspace successfully created with Resource Id: {DBX_WORKSPACE_URL}')

        print('updating secrets to KeyVault: Workspace id and Workspace url')
        #az_cli(f'keyvault secret set --name dbx-workspace-id --vault-name {DBX_VAULT} --value {DBX_RESOURCE_ID}')
        #az_cli(f'keyvault secret set --name dbx-workspace-url --vault-name {DBX_VAULT} --value {DBX_WORKSPACE_URL}')

    except getopt.GetoptError:
        print(USAGE_MSJ)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])