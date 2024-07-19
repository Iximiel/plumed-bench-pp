# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def _append_kernel_rec(keys: "list[str] | Iterable[str]", name: str, level: int) -> str:
    nm = name if level == 0 else f"{name}({level})"
    if nm in keys:
        return _append_kernel_rec(keys, name, level + 1)
    return nm

def _common_iterable(obj):
        """Iterates over the values of a dict or any iterable"""
        if isinstance(obj, dict):
            yield from obj.values()
        else:
            yield from obj


def kernel_name(data: dict, name: str) -> str:
    return _append_kernel_rec(data.keys(), name, 0)


# TODO: add a extract filenames extract and extract kernel+file combination

def get_kernels(data: dict) -> set[str]:
    toret=[]
    if isinstance(data, dict) and "BENCHSETTINGS" in data.keys():
        data=[data]
    for d in _common_iterable(data):
        for k in d:
            if k == "BENCHSETTINGS":
                continue
            toret.append(d[k]["kernel"])

    return set(toret)

def get_files(data: dict) -> set[str]: