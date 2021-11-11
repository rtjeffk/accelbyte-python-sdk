# justice-iam-service (4.7.0)

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
from ....api.iam import admin_list_assigned_users_v4 as admin_list_assigned_users_v4_internal
from ....api.iam.models import ModelListAssignedUsersV4Response
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("role_id", type=str)
@click.option("--after", "after", type=str)
@click.option("--before", "before", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def admin_list_assigned_users_v4(
        role_id: str,
        after: Optional[str] = None,
        before: Optional[str] = None,
        limit: Optional[int] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(admin_list_assigned_users_v4_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = admin_list_assigned_users_v4_internal(
        role_id=role_id,
        after=after,
        before=before,
        limit=limit,
    )
    if error:
        raise Exception(f"AdminListAssignedUsersV4 failed: {str(error)}")
    click.echo("AdminListAssignedUsersV4 success")
