"""Auto-generated package that contains utility functions for the justice-social-service."""

__version__ = "1.23.0"
__author__ = "AccelByte"
__email__ = "dev@accelbyte.net"

# template file: justice_py_sdk_codegen/__main__.py

# pylint: disable=line-too-long

from ._game_profile import get_profile
from ._game_profile import get_profile_async
from ._game_profile import get_user_profiles
from ._game_profile import get_user_profiles_async
from ._game_profile import public_create_profile
from ._game_profile import public_create_profile_async
from ._game_profile import public_delete_profile
from ._game_profile import public_delete_profile_async
from ._game_profile import public_get_profile
from ._game_profile import public_get_profile_async
from ._game_profile import public_get_profile_attribute
from ._game_profile import public_get_profile_attribute_async
from ._game_profile import public_get_user_game_profiles
from ._game_profile import public_get_user_game_profiles_async
from ._game_profile import public_get_user_profiles
from ._game_profile import public_get_user_profiles_async
from ._game_profile import public_update_attribute
from ._game_profile import public_update_attribute_async
from ._game_profile import public_update_profile
from ._game_profile import public_update_profile_async

from ._global_statistic import get_global_stat_items
from ._global_statistic import get_global_stat_items_async

from ._slot import get_slot_data
from ._slot import get_slot_data_async
from ._slot import get_user_namespace_slots
from ._slot import get_user_namespace_slots_async
from ._slot import public_create_user_namespace_slot
from ._slot import public_create_user_namespace_slot_async
from ._slot import public_delete_user_namespace_slot
from ._slot import public_delete_user_namespace_slot_async
from ._slot import public_get_slot_data
from ._slot import public_get_slot_data_async
from ._slot import public_get_user_namespace_slots
from ._slot import public_get_user_namespace_slots_async
from ._slot import public_update_user_namespace_slot
from ._slot import public_update_user_namespace_slot_async
from ._slot import public_update_user_namespace_slot_metadata
from ._slot import public_update_user_namespace_slot_metadata_async

from ._slot_config import delete_namespace_slot_config
from ._slot_config import delete_namespace_slot_config_async
from ._slot_config import delete_user_slot_config
from ._slot_config import delete_user_slot_config_async
from ._slot_config import get_namespace_slot_config
from ._slot_config import get_namespace_slot_config_async
from ._slot_config import get_user_slot_config
from ._slot_config import get_user_slot_config_async
from ._slot_config import update_namespace_slot_config
from ._slot_config import update_namespace_slot_config_async
from ._slot_config import update_user_slot_config
from ._slot_config import update_user_slot_config_async

from ._stat_configuration import create_stat
from ._stat_configuration import create_stat_async
from ._stat_configuration import create_stat_1
from ._stat_configuration import create_stat_1_async
from ._stat_configuration import delete_stat
from ._stat_configuration import delete_stat_async
from ._stat_configuration import export_stats
from ._stat_configuration import export_stats_async
from ._stat_configuration import get_stat
from ._stat_configuration import get_stat_async
from ._stat_configuration import get_stats
from ._stat_configuration import get_stats_async
from ._stat_configuration import import_stats
from ._stat_configuration import import_stats_async
from ._stat_configuration import query_stats
from ._stat_configuration import query_stats_async
from ._stat_configuration import update_stat
from ._stat_configuration import update_stat_async

from ._user_statistic import bulk_create_user_stat_items
from ._user_statistic import bulk_create_user_stat_items_async
from ._user_statistic import bulk_fetch_stat_items
from ._user_statistic import bulk_fetch_stat_items_async
from ._user_statistic import bulk_fetch_stat_items_1
from ._user_statistic import bulk_fetch_stat_items_1_async
from ._user_statistic import bulk_inc_user_stat_item
from ._user_statistic import bulk_inc_user_stat_item_async
from ._user_statistic import bulk_inc_user_stat_item_1
from ._user_statistic import bulk_inc_user_stat_item_1_async
from ._user_statistic import bulk_inc_user_stat_item_value
from ._user_statistic import bulk_inc_user_stat_item_value_async
from ._user_statistic import bulk_inc_user_stat_item_value_1
from ._user_statistic import bulk_inc_user_stat_item_value_1_async
from ._user_statistic import bulk_inc_user_stat_item_value_2
from ._user_statistic import bulk_inc_user_stat_item_value_2_async
from ._user_statistic import bulk_reset_user_stat_item
from ._user_statistic import bulk_reset_user_stat_item_async
from ._user_statistic import bulk_reset_user_stat_item_1
from ._user_statistic import bulk_reset_user_stat_item_1_async
from ._user_statistic import bulk_reset_user_stat_item_2
from ._user_statistic import bulk_reset_user_stat_item_2_async
from ._user_statistic import bulk_reset_user_stat_item_3
from ._user_statistic import bulk_reset_user_stat_item_3_async
from ._user_statistic import bulk_update_user_stat_item
from ._user_statistic import bulk_update_user_stat_item_async
from ._user_statistic import bulk_update_user_stat_item_1
from ._user_statistic import bulk_update_user_stat_item_1_async
from ._user_statistic import bulk_update_user_stat_item_2
from ._user_statistic import bulk_update_user_stat_item_2_async
from ._user_statistic import bulk_update_user_stat_item_v2
from ._user_statistic import bulk_update_user_stat_item_v2_async
from ._user_statistic import create_user_stat_item
from ._user_statistic import create_user_stat_item_async
from ._user_statistic import delete_user_stat_items
from ._user_statistic import delete_user_stat_items_async
from ._user_statistic import delete_user_stat_items_1
from ._user_statistic import delete_user_stat_items_1_async
from ._user_statistic import delete_user_stat_items_2
from ._user_statistic import delete_user_stat_items_2_async
from ._user_statistic import get_user_stat_items
from ._user_statistic import get_user_stat_items_async
from ._user_statistic import inc_user_stat_item_value
from ._user_statistic import inc_user_stat_item_value_async
from ._user_statistic import public_bulk_create_user_stat_items
from ._user_statistic import public_bulk_create_user_stat_items_async
from ._user_statistic import public_bulk_inc_user_stat_item
from ._user_statistic import public_bulk_inc_user_stat_item_async
from ._user_statistic import public_bulk_inc_user_stat_item_1
from ._user_statistic import public_bulk_inc_user_stat_item_1_async
from ._user_statistic import public_bulk_inc_user_stat_item_value
from ._user_statistic import public_bulk_inc_user_stat_item_value_async
from ._user_statistic import public_create_user_stat_item
from ._user_statistic import public_create_user_stat_item_async
from ._user_statistic import public_inc_user_stat_item
from ._user_statistic import public_inc_user_stat_item_async
from ._user_statistic import public_inc_user_stat_item_value
from ._user_statistic import public_inc_user_stat_item_value_async
from ._user_statistic import public_query_user_stat_items
from ._user_statistic import public_query_user_stat_items_async
from ._user_statistic import reset_user_stat_item_value
from ._user_statistic import reset_user_stat_item_value_async
from ._user_statistic import reset_user_stat_item_value_1
from ._user_statistic import reset_user_stat_item_value_1_async
from ._user_statistic import update_user_stat_item_value
from ._user_statistic import update_user_stat_item_value_async
from ._user_statistic import update_user_stat_item_value_1
from ._user_statistic import update_user_stat_item_value_1_async
