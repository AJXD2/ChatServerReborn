from dataclasses import dataclass
from common.classes.flags import Flags

from common.classes.permission import PermissionManager


@dataclass
class User:
    name: str
    uuid: str | bytes
    permissions = PermissionManager()
    flags = Flags()
    extra = {}
