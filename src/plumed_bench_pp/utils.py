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


def kernel_name(data: dict, name: str) -> str:
    return _append_kernel_rec(data.keys(), name, 0)
