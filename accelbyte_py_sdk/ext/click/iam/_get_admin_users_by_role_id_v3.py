import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import get_admin_users_by_role_id_v3 as get_admin_users_by_role_id_v3_internal
from ....api.iam.models import ModelGetUsersResponseWithPaginationV3
from ....api.iam.models import RestapiErrorResponse


@click.command()
@click.argument("role_id", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--after", "after", type=int)
@click.option("--before", "before", type=int)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_admin_users_by_role_id_v3(
        role_id: str,
        limit: Optional[int] = None,
        after: Optional[int] = None,
        before: Optional[int] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_admin_users_by_role_id_v3_internal.__doc__)
    result, error = get_admin_users_by_role_id_v3_internal(
        role_id=role_id,
        limit=limit,
        after=after,
        before=before,
        namespace=namespace,
    )
    if error:
        raise Exception(f"GetAdminUsersByRoleIdV3 failed: {str(error)}")
    click.echo("GetAdminUsersByRoleIdV3 success")