# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template_file: python-cli-command.j2

# justice-platform-service (4.2.0)

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
from accelbyte_py_sdk.api.platform import update_key_group as update_key_group_internal
from accelbyte_py_sdk.api.platform.models import ErrorEntity
from accelbyte_py_sdk.api.platform.models import KeyGroupInfo
from accelbyte_py_sdk.api.platform.models import KeyGroupUpdate
from accelbyte_py_sdk.api.platform.models import ValidationErrorEntity


@click.command()
@click.argument("key_group_id", type=str)
@click.option("--body", "body", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--login_with_auth", type=str)
@click.option("--doc", type=bool)
def update_key_group(
        key_group_id: str,
        body: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        login_with_auth: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(update_key_group_internal.__doc__)
        return
    x_additional_headers = None
    if login_with_auth:
        x_additional_headers = {
            "Authorization": login_with_auth
        }
    else:
        login_as_internal(login_as)
    if body is not None:
        try:
            body_json = json.loads(body)
            body = KeyGroupUpdate.create_from_dict(body_json)
        except ValueError as e:
            raise Exception(f"Invalid JSON for 'body'. {str(e)}") from e
    _, error = update_key_group_internal(
        key_group_id=key_group_id,
        body=body,
        namespace=namespace,
        x_additional_headers=x_additional_headers,
    )
    if error:
        raise Exception(f"updateKeyGroup failed: {str(error)}")
    click.echo("updateKeyGroup success")
