from azure.cli.core import get_default_cli

az_cli = get_default_cli()

result = az_cli.invoke(['group', 'list'])

output1 = result.

print(result)