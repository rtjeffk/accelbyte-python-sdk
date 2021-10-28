import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import admin_delete_role_permission_v3 as admin_delete_role_permission_v3_internal
from ....api.iam.models import RestapiErrorResponse


@click.command()
@click.argument("role_id", type=str)
@click.argument("resource", type=str)
@click.argument("action", type=int)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def admin_delete_role_permission_v3(
        role_id: str,
        resource: str,
        action: int,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(admin_delete_role_permission_v3_internal.__doc__)
    result, error = admin_delete_role_permission_v3_internal(
        role_id=role_id,
        resource=resource,
        action=action,
    )
    if error:
        raise Exception(f"AdminDeleteRolePermissionV3 failed: {str(error)}")
    click.echo("AdminDeleteRolePermissionV3 success")