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
from ....api.platform import feature_item as feature_item_internal
from ....api.platform.models import ErrorEntity
from ....api.platform.models import FullItemInfo


@click.command()
@click.argument("feature", type=str)
@click.argument("item_id", type=str)
@click.argument("store_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def feature_item(
        feature: str,
        item_id: str,
        store_id: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(feature_item_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = feature_item_internal(
        feature=feature,
        item_id=item_id,
        store_id=store_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"featureItem failed: {str(error)}")
    click.echo("featureItem success")
