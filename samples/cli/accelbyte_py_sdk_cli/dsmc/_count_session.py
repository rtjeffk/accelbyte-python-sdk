# justice-dsm-controller-service (2.11.0)

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
from accelbyte_py_sdk.api.dsmc import count_session as count_session_internal
from accelbyte_py_sdk.api.dsmc.models import ModelsCountSessionResponse
from accelbyte_py_sdk.api.dsmc.models import ResponseError


@click.command()
@click.option("--region", "region", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def count_session(
        region: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(count_session_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = count_session_internal(
        region=region,
        namespace=namespace,
    )
    if error:
        raise Exception(f"CountSession failed: {str(error)}")
    click.echo("CountSession success")