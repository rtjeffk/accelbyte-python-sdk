import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import reset_password as reset_password_internal
from ....api.iam.models import ModelResetPasswordRequest


@click.command()
@click.argument("body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def reset_password(
        body: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(reset_password_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = ModelResetPasswordRequest.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = reset_password_internal(
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"ResetPassword failed: {str(error)}")
    click.echo("ResetPassword success")
