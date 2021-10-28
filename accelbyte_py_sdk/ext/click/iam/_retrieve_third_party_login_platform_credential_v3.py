import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import retrieve_third_party_login_platform_credential_v3 as retrieve_third_party_login_platform_credential_v3_internal
from ....api.iam.models import ModelThirdPartyLoginPlatformCredentialResponse
from ....api.iam.models import RestErrorResponse


@click.command()
@click.argument("platform_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def retrieve_third_party_login_platform_credential_v3(
        platform_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(retrieve_third_party_login_platform_credential_v3_internal.__doc__)
    result, error = retrieve_third_party_login_platform_credential_v3_internal(
        platform_id=platform_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"RetrieveThirdPartyLoginPlatformCredentialV3 failed: {str(error)}")
    click.echo("RetrieveThirdPartyLoginPlatformCredentialV3 success")
