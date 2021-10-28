import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import token_introspection_v3 as token_introspection_v3_internal
from ....api.iam.models import OauthmodelErrorResponse
from ....api.iam.models import OauthmodelTokenIntrospectResponse


@click.command()
@click.argument("token", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def token_introspection_v3(
        token: str,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(token_introspection_v3_internal.__doc__)
    result, error = token_introspection_v3_internal(
        token=token,
    )
    if error:
        raise Exception(f"TokenIntrospectionV3 failed: {str(error)}")
    click.echo("TokenIntrospectionV3 success")
