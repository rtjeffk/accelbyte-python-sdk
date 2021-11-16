# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
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

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import run_request_async
from ....core import same_doc_as

from ..models import ErrorEntity

from ..operations.anonymization import AnonymizeUserAgreement


@same_doc_as(AnonymizeUserAgreement)
def anonymize_user_agreement(user_id: str, x_additional_headers: Optional[Dict[str, str]] = None):
    request = AnonymizeUserAgreement.create(
        user_id=user_id,
    )
    return run_request(request, additional_headers=x_additional_headers)


@same_doc_as(AnonymizeUserAgreement)
async def anonymize_user_agreement_async(user_id: str, x_additional_headers: Optional[Dict[str, str]] = None):
    request = AnonymizeUserAgreement.create(
        user_id=user_id,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)
