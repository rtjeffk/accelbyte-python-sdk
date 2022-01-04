# justice-social-service (1.22.1)

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
from accelbyte_py_sdk.api.social import create_user_stat_item as create_user_stat_item_internal
from accelbyte_py_sdk.api.social.models import ErrorEntity


@click.command()
@click.argument("stat_code", type=str)
@click.argument("user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def create_user_stat_item(
        stat_code: str,
        user_id: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(create_user_stat_item_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = create_user_stat_item_internal(
        stat_code=stat_code,
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"createUserStatItem failed: {str(error)}")
    click.echo("createUserStatItem success")