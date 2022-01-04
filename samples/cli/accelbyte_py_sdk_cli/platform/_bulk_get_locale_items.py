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
from accelbyte_py_sdk.api.platform import bulk_get_locale_items as bulk_get_locale_items_internal
from accelbyte_py_sdk.api.platform.models import ErrorEntity
from accelbyte_py_sdk.api.platform.models import ItemInfo


@click.command()
@click.argument("item_ids", type=str)
@click.option("--active_only", "active_only", type=bool)
@click.option("--language", "language", type=str)
@click.option("--region", "region", type=str)
@click.option("--store_id", "store_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def bulk_get_locale_items(
        item_ids: str,
        active_only: Optional[bool] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
        store_id: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(bulk_get_locale_items_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = bulk_get_locale_items_internal(
        item_ids=item_ids,
        active_only=active_only,
        language=language,
        region=region,
        store_id=store_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"bulkGetLocaleItems failed: {str(error)}")
    click.echo("bulkGetLocaleItems success")