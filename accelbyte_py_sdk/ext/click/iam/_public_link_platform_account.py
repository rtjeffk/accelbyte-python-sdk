import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import public_link_platform_account as public_link_platform_account_internal
from ....api.iam.models import ModelLinkPlatformAccountRequest
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("body", type=str)
@click.argument("user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def public_link_platform_account(
        body: str,
        user_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(public_link_platform_account_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = ModelLinkPlatformAccountRequest.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = public_link_platform_account_internal(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"PublicLinkPlatformAccount failed: {str(error)}")
    click.echo("PublicLinkPlatformAccount success")