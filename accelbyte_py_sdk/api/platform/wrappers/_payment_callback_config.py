# template file: justice_py_sdk_codegen/__main__.py

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
from ..models import PaymentCallbackConfigInfo
from ..models import PaymentCallbackConfigUpdate

from ..operations.payment_callback_config import GetPaymentCallbackConfig
from ..operations.payment_callback_config import UpdatePaymentCallbackConfig


@same_doc_as(GetPaymentCallbackConfig)
def get_payment_callback_config(namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetPaymentCallbackConfig.create(
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@same_doc_as(GetPaymentCallbackConfig)
async def get_payment_callback_config_async(namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetPaymentCallbackConfig.create(
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)


@same_doc_as(UpdatePaymentCallbackConfig)
def update_payment_callback_config(body: Optional[PaymentCallbackConfigUpdate] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdatePaymentCallbackConfig.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@same_doc_as(UpdatePaymentCallbackConfig)
async def update_payment_callback_config_async(body: Optional[PaymentCallbackConfigUpdate] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdatePaymentCallbackConfig.create(
        body=body,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)