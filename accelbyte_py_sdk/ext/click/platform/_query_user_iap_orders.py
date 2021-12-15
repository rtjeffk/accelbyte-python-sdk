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
from ....api.platform import query_user_iap_orders as query_user_iap_orders_internal
from ....api.platform.models import IAPOrderPagingSlicedResult


@click.command()
@click.argument("user_id", type=str)
@click.option("--end_time", "end_time", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--product_id", "product_id", type=str)
@click.option("--start_time", "start_time", type=str)
@click.option("--status", "status", type=str)
@click.option("--type", "type_", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def query_user_iap_orders(
        user_id: str,
        end_time: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        product_id: Optional[str] = None,
        start_time: Optional[str] = None,
        status: Optional[str] = None,
        type_: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(query_user_iap_orders_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = query_user_iap_orders_internal(
        user_id=user_id,
        end_time=end_time,
        limit=limit,
        offset=offset,
        product_id=product_id,
        start_time=start_time,
        status=status,
        type_=type_,
        namespace=namespace,
    )
    if error:
        raise Exception(f"queryUserIAPOrders failed: {str(error)}")
    click.echo("queryUserIAPOrders success")
