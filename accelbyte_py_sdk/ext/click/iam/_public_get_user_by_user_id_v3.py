import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import public_get_user_by_user_id_v3 as public_get_user_by_user_id_v3_internal
from ....api.iam.models import ModelPublicUserResponseV3
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def public_get_user_by_user_id_v3(
        user_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(public_get_user_by_user_id_v3_internal.__doc__)
    result, error = public_get_user_by_user_id_v3_internal(
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"PublicGetUserByUserIdV3 failed: {str(error)}")
    click.echo("PublicGetUserByUserIdV3 success")
