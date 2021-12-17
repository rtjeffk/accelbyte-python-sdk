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
from accelbyte_py_sdk.api.platform import public_get_my_entitlement_ownership_by_item_id as public_get_my_entitlement_ownership_by_item_id_internal
from accelbyte_py_sdk.api.platform.models import TimedOwnership


@click.command()
@click.argument("item_id", type=str)
@click.option("--entitlement_clazz", "entitlement_clazz", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def public_get_my_entitlement_ownership_by_item_id(
        item_id: str,
        entitlement_clazz: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(public_get_my_entitlement_ownership_by_item_id_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = public_get_my_entitlement_ownership_by_item_id_internal(
        item_id=item_id,
        entitlement_clazz=entitlement_clazz,
        namespace=namespace,
    )
    if error:
        raise Exception(f"publicGetMyEntitlementOwnershipByItemId failed: {str(error)}")
    click.echo("publicGetMyEntitlementOwnershipByItemId success")
