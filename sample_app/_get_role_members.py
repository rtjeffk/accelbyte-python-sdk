import yaml

import click

from accelbyte_py_sdk.api.iam import admin_get_role_members_v3

from ._utils import login_user


@click.command()
@click.argument("role_id")
@click.argument("limit", type=int)
@click.argument("before")
@click.argument("after")
@click.option("--doc", type=bool)
def get_role_members(
        role_id,
        limit,
        before,
        after,
        doc,
):
    login_user(None, None)
    if doc:
        click.echo(admin_get_role_members_v3.__doc__)
    result, error = admin_get_role_members_v3(
        role_id=role_id,
        limit=limit,
        after=after,
        before=before,
    )
    if error:
        raise Exception(str(error))
    click.echo("Get role members success.")
    click.echo(yaml.safe_dump(result.to_dict()))