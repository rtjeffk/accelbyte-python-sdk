import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import admin_get_role_admin_status_v3 as admin_get_role_admin_status_v3_internal
from ....api.iam.models import ModelRoleAdminStatusResponseV3
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("role_id", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def admin_get_role_admin_status_v3(
        role_id: str,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(admin_get_role_admin_status_v3_internal.__doc__)
    result, error = admin_get_role_admin_status_v3_internal(
        role_id=role_id,
    )
    if error:
        raise Exception(f"AdminGetRoleAdminStatusV3 failed: {str(error)}")
    click.echo("AdminGetRoleAdminStatusV3 success")
