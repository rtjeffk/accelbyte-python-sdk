import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import update_role_permissions as update_role_permissions_internal
from ....api.iam.models import AccountcommonPermissions


@click.command()
@click.argument("body", type=str)
@click.argument("role_id", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def update_role_permissions(
        body: str,
        role_id: str,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(update_role_permissions_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = AccountcommonPermissions.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = update_role_permissions_internal(
        body=body,
        role_id=role_id,
    )
    if error:
        raise Exception(f"UpdateRolePermissions failed: {str(error)}")
    click.echo("UpdateRolePermissions success")