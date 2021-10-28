import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import admin_create_client_v3 as admin_create_client_v3_internal
from ....api.iam.models import ClientmodelClientCreationV3Request
from ....api.iam.models import ClientmodelClientV3Response
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def admin_create_client_v3(
        body: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(admin_create_client_v3_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = ClientmodelClientCreationV3Request.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = admin_create_client_v3_internal(
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"AdminCreateClientV3 failed: {str(error)}")
    click.echo("AdminCreateClientV3 success")
