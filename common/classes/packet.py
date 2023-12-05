from dataclasses import dataclass
import json
from time import time

from common.classes.flags import Flags


@dataclass
class Packet:
    type = "unknown"
    sendtime = 0
    recvtime = 0
    data = {}
    flags = Flags()

    def load_from_dict(self, data):
        data = data if isinstance(data, dict) else json.loads(data)

        pending = {}

        pending["type"] = data.get("type")
        pending["sendtime"] = data.get("meta", {}).get("sendtime")
        pending["recvtime"] = time()
        pending["data"] = data.get("data")
        pending["flags"] = Flags(data.get("flags", []))

        if None in pending.values():
            raise ValueError("Insufficient data.")

        self.data = pending.copy()
        del pending
