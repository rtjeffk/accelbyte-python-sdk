# justice-seasonpass-service (1.5.0)

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
from ....api.seasonpass import public_bulk_claim_user_rewards as public_bulk_claim_user_rewards_internal
from ....api.seasonpass.models import ClaimableRewards
from ....api.seasonpass.models import ErrorEntity


@click.command()
@click.argument("user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def public_bulk_claim_user_rewards(
        user_id: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(public_bulk_claim_user_rewards_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = public_bulk_claim_user_rewards_internal(
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"publicBulkClaimUserRewards failed: {str(error)}")
    click.echo("publicBulkClaimUserRewards success")
