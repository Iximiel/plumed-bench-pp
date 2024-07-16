# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT


from plumed_bench_pp.constants import (
    TIMINGCOLS,
)


def extract_row(
    data: dict,
    rows: list,
) -> "dict[str, dict[str,list]]":
    """
    Extracts the specified rows from the given data dictionary.
    Works with the results of plumed_bench_pp.parser.parse_benchmark_output

    Args:
        data (dict): The input dictionary containing data.
        rows (list): The list of rows to extract.

    Returns:
        dict[str, dict[str,list]]: A dictionary of the simulations.
    """
    df = {}
    for key in data:
        if key == "BENCHSETTINGS":
            continue
        tmp = {}
        for row in rows:
            tmp[row] = [data[key][row][timing_col] for timing_col in TIMINGCOLS]
        df[key] = tmp

    return df
