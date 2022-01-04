# justice-platform-service (3.40.0)

# Copyright (c) 2018 - 2022 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template_file: python-cli-command.j2

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from accelbyte_py_sdk.api.platform import query_entitlements as query_entitlements_internal
from accelbyte_py_sdk.api.platform.models import EntitlementPagingSlicedResult


@click.command()
@click.option("--active_only", "active_only", type=bool)
@click.option("--app_type", "app_type", type=str)
@click.option("--entitlement_clazz", "entitlement_clazz", type=str)
@click.option("--entitlement_name", "entitlement_name", type=str)
@click.option("--item_id", "item_id", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--user_id", "user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def query_entitlements(
        active_only: Optional[bool] = None,
        app_type: Optional[str] = None,
        entitlement_clazz: Optional[str] = None,
        entitlement_name: Optional[str] = None,
        item_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        user_id: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(query_entitlements_internal.__doc__)
        return
    login_as_internal(login_as)
    if item_id is not None:
        try:
            item_id_json = json.loads(item_id)
            item_id = [str(i0) for i0 in item_id_json]
        except ValueError as e:
            raise Exception(f"Invalid JSON for 'itemId'. {str(e)}") from e
    _, error = query_entitlements_internal(
        active_only=active_only,
        app_type=app_type,
        entitlement_clazz=entitlement_clazz,
        entitlement_name=entitlement_name,
        item_id=item_id,
        limit=limit,
        offset=offset,
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"queryEntitlements failed: {str(error)}")
    click.echo("queryEntitlements success")