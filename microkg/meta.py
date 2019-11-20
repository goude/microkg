import collections
import datetime
import re
from typing import Callable, Dict, Iterable

Meta = collections.namedtuple("Meta", "name validation")


def get_delimiter(k) -> str:
    delimiters = dict(space=" ")
    return delimiters.get(k, k)


def get_type(t: str) -> Callable:
    types: Dict[str, Callable] = {
        "date": lambda d: datetime.datetime.strptime(d, "%Y-%m-%d"),
        "str": str,
    }
    return types[t]


def get_meta_value(name: str, val: str) -> Iterable:
    meta = {
        m.name: m
        for m in [
            Meta(name="version", validation=r"^v\d+.\d+.\d+$"),
            Meta(name="delimiter", validation="^[a-z_]+$"),
            Meta(name="columns", validation="^[a-z_]+( [a-z_]+)*$"),
            Meta(name="types", validation="^[a-z_]+( [a-z_]+)*$"),
            Meta(name="validations", validation="^.+$"),
        ]
    }

    m = meta[name]

    if not re.match(m.validation, val):
        raise RuntimeError(f"Validation {m.validation} failed for {m} {val}")

    meta_separator = " "

    if meta_separator in val:
        return val.split(meta_separator)
    else:
        return val
