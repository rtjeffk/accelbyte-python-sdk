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
from accelbyte_py_sdk.api.legal import request_presigned_url as request_presigned_url_internal
from accelbyte_py_sdk.api.legal.models import ErrorEntity
from accelbyte_py_sdk.api.legal.models import UploadLocalizedPolicyVersionAttachmentResponse
from accelbyte_py_sdk.api.legal.models import UploadPolicyVersionAttachmentRequest


@click.command()
@click.argument("localized_policy_version_id", type=str)
@click.option("--body", "body", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def request_presigned_url(
        localized_policy_version_id: str,
        body: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(request_presigned_url_internal.__doc__)
        return
    login_as_internal(login_as)
    if body is not None:
        try:
            body_json = json.loads(body)
            body = UploadPolicyVersionAttachmentRequest.create_from_dict(body_json)
        except ValueError as e:
            raise Exception(f"Invalid JSON for 'body'. {str(e)}") from e
    _, error = request_presigned_url_internal(
        localized_policy_version_id=localized_policy_version_id,
        body=body,
    )
    if error:
        raise Exception(f"requestPresignedURL failed: {str(error)}")
    click.echo("requestPresignedURL success")