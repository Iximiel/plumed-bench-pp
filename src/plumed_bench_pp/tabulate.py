# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT


from plumed_bench_pp.constants import (
    TIMINGCOLS,
)


def extract_row(
    data: dict,
    cols: list,
) -> "dict[str, list]":
    df: dict[str, list] = {}
    for key in data:
        if key == "BENCHSETTINGS":
            continue
        loc = f'{key}+{data[key]["input"]}'
        df[loc] = {}
        for col in cols:
            t = [data[key][col][timing_col] for timing_col in TIMINGCOLS]
            df[loc][col] = t

    return df
