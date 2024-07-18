# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT


import re

from pandas import DataFrame

from plumed_bench_pp.constants import (
    TIMINGCOLS,
)


def extract_rows(data: dict, rows: list) -> "dict[str, dict[str,list]]":
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


def _checkfile(fname: str, pattern: "str|list[str]|re.Pattern") -> bool:
    if isinstance(pattern, list):
        return fname in pattern
    if isinstance(pattern, re.Pattern):
        return pattern.search(fname) is not None
    return pattern in fname


def convert_to_table(
    filesdict: dict, rows_to_extract: list[str], kernel: str, inputlist: "str|list[str]|re.Pattern"
) -> "dict[str,DataFrame]":
    data: dict[str, DataFrame] = {}
    tmp: dict = {}
    for row in rows_to_extract:
        tmp[row] = []
    for fname in filesdict:
        file = filesdict[fname]
        key = None
        for k in file:
            if k == "BENCHSETTINGS":
                continue
            if (file[k]["kernel"] == kernel) and _checkfile(file[k]["input"], inputlist):
                key = k
                break

        if key is None:
            # print warning
            continue
        natoms = file["BENCHSETTINGS"]["BENCHATOMS"]

        tt = extract_rows(file, rows_to_extract)
        for row in rows_to_extract:
            tmp[row].append([natoms, *tt[key][row]])

    for row in rows_to_extract:
        data[row] = DataFrame(tmp[row], columns=["natoms", *TIMINGCOLS])
    return data
