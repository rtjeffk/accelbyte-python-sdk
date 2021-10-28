import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import public_query_user_entitlements_by_app_type as public_query_user_entitlements_by_app_type_internal
from ....api.platform.models import AppEntitlementPagingSlicedResult


@click.command()
@click.argument("user_id", type=str)
@click.argument("app_type", type=str)
@click.option("--offset", "offset", type=int)
@click.option("--limit", "limit", type=int)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def public_query_user_entitlements_by_app_type(
        user_id: str,
        app_type: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(public_query_user_entitlements_by_app_type_internal.__doc__)
    result, error = public_query_user_entitlements_by_app_type_internal(
        user_id=user_id,
        app_type=app_type,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    if error:
        raise Exception(f"publicQueryUserEntitlementsByAppType failed: {str(error)}")
    click.echo("publicQueryUserEntitlementsByAppType success")