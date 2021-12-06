import yaml

import click

from accelbyte_py_sdk.api.iam import admin_get_role_v3

from ._utils import login_as as login_as_internal


@click.command()
@click.argument("role_id")
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_role_by_id(
        role_id,
        doc,
        login_as,
):
    login_as_internal(login_as)
    if doc:
        click.echo(admin_get_role_v3.__doc__)
    result, error = admin_get_role_v3(
        role_id=role_id,
    )
    if error:
        raise Exception(str(error))
    click.echo("Get role by id success.")
    click.echo(yaml.safe_dump(result.to_dict()))