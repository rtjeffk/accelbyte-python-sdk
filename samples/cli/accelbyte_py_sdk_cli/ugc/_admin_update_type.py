# justice-ugc-service (1.10.1)

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
from accelbyte_py_sdk.api.ugc import admin_update_type as admin_update_type_internal
from accelbyte_py_sdk.api.ugc.models import ModelsCreateTypeRequest
from accelbyte_py_sdk.api.ugc.models import ModelsCreateTypeResponse
from accelbyte_py_sdk.api.ugc.models import ResponseError


@click.command()
@click.argument("body", type=str)
@click.argument("type_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def admin_update_type(
        body: str,
        type_id: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(admin_update_type_internal.__doc__)
        return
    login_as_internal(login_as)
    if body is not None:
        try:
            body_json = json.loads(body)
            body = ModelsCreateTypeRequest.create_from_dict(body_json)
        except ValueError as e:
            raise Exception(f"Invalid JSON for 'body'. {str(e)}") from e
    _, error = admin_update_type_internal(
        body=body,
        type_id=type_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"AdminUpdateType failed: {str(error)}")
    click.echo("AdminUpdateType success")