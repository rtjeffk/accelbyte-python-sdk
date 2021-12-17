# justice-platform-service (3.39.0)

# Copyright (c) 2018 - 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

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
from accelbyte_py_sdk.api.platform import exists_any_user_active_entitlement_by_item_ids as exists_any_user_active_entitlement_by_item_ids_internal
from accelbyte_py_sdk.api.platform.models import Ownership


@click.command()
@click.argument("user_id", type=str)
@click.argument("item_ids", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def exists_any_user_active_entitlement_by_item_ids(
        user_id: str,
        item_ids: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(exists_any_user_active_entitlement_by_item_ids_internal.__doc__)
        return
    login_as_internal(login_as)
    try:
        item_ids_json = json.loads(item_ids)
        item_ids = [str(i0) for i0 in item_ids_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'itemIds'. {str(e)}") from e
    _, error = exists_any_user_active_entitlement_by_item_ids_internal(
        user_id=user_id,
        item_ids=item_ids,
        namespace=namespace,
    )
    if error:
        raise Exception(f"existsAnyUserActiveEntitlementByItemIds failed: {str(error)}")
    click.echo("existsAnyUserActiveEntitlementByItemIds success")
