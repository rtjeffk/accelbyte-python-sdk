# justice-legal-service (1.15.1)

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
from accelbyte_py_sdk.api.legal import retrieve_latest_policies_by_namespace_and_country_public as retrieve_latest_policies_by_namespace_and_country_public_internal
from accelbyte_py_sdk.api.legal.models import RetrievePolicyPublicResponse


@click.command()
@click.argument("country_code", type=str)
@click.option("--always_include_default", "always_include_default", type=bool)
@click.option("--default_on_empty", "default_on_empty", type=bool)
@click.option("--policy_type", "policy_type", type=str)
@click.option("--tags", "tags", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def retrieve_latest_policies_by_namespace_and_country_public(
        country_code: str,
        always_include_default: Optional[bool] = None,
        default_on_empty: Optional[bool] = None,
        policy_type: Optional[str] = None,
        tags: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(retrieve_latest_policies_by_namespace_and_country_public_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = retrieve_latest_policies_by_namespace_and_country_public_internal(
        country_code=country_code,
        always_include_default=always_include_default,
        default_on_empty=default_on_empty,
        policy_type=policy_type,
        tags=tags,
        namespace=namespace,
    )
    if error:
        raise Exception(f"retrieveLatestPoliciesByNamespaceAndCountryPublic failed: {str(error)}")
    click.echo("retrieveLatestPoliciesByNamespaceAndCountryPublic success")
