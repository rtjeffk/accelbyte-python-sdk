# justice-achievement-service ()

# Copyright (c) 2018 - 2022 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template_file: python-cli-init.j2

from ._admin_list_achievements import admin_list_achievements
from ._admin_create_new_achievement import admin_create_new_achievement
from ._export_achievements import export_achievements
from ._import_achievements import import_achievements
from ._admin_get_achievement import admin_get_achievement
from ._admin_update_achievement import admin_update_achievement
from ._admin_delete_achievement import admin_delete_achievement
from ._admin_update_achievement_list_order import admin_update_achievement_list_order
from ._admin_list_user_achievements import admin_list_user_achievements
from ._admin_unlock_achievement import admin_unlock_achievement
from ._public_list_achievements import public_list_achievements
from ._public_get_achievement import public_get_achievement
from ._public_list_user_achievements import public_list_user_achievements
from ._public_unlock_achievement import public_unlock_achievement


commands = [
    admin_list_achievements,
    admin_create_new_achievement,
    export_achievements,
    import_achievements,
    admin_get_achievement,
    admin_update_achievement,
    admin_delete_achievement,
    admin_update_achievement_list_order,
    admin_list_user_achievements,
    admin_unlock_achievement,
    public_list_achievements,
    public_get_achievement,
    public_list_user_achievements,
    public_unlock_achievement,
]