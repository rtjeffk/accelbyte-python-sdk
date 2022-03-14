# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

"""Auto-generated package that contains models used by the justice-ds-log-manager-service."""

__version__ = "2.1.0"
__author__ = "AccelByte"
__email__ = "dev@accelbyte.net"

# pylint: disable=line-too-long

from ._all_terminated_servers import batch_download_server_logs
from ._all_terminated_servers import batch_download_server_logs_async
from ._all_terminated_servers import list_all_terminated_servers
from ._all_terminated_servers import list_all_terminated_servers_async

from ._operations import public_get_messages
from ._operations import public_get_messages_async

from ._terminated_servers import check_server_logs
from ._terminated_servers import check_server_logs_async
from ._terminated_servers import download_server_logs
from ._terminated_servers import download_server_logs_async
from ._terminated_servers import list_terminated_servers
from ._terminated_servers import list_terminated_servers_async
