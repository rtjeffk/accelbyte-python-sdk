from io import StringIO
from collections import UserDict


class HeaderStr(UserDict):

    def __str__(self):
        sio = StringIO()
        first = True
        for k, v in self.items():
            if not first:
                sio.write("; ")
            v = str(v)
            if not v:
                continue
            first = False
            sio.write(f"{k}={self[k]}")
        return sio.getvalue()

    @classmethod
    def create_from_str(cls, string: str):
        instance = cls()
        parts = string.split("; ")
        for part in parts:
            key_value = part.split("=", maxsplit=1)
            if len(key_value) != 2:
                raise ValueError()
            key, value = key_value
            instance[key] = value
        return instance
