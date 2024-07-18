# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT


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


def convert_to_table(filesdict, rows_to_extract, kernel, inputlist):
    data = {}
    for row in rows_to_extract:
        data[row] = []
    for fname in filesdict:
        file = filesdict[fname]
        key = None
        for k in file:
            if k == "BENCHSETTINGS":
                continue
            if (file[k]["kernel"] == kernel) and (file[k]["input"] in inputlist):
                key = k
                break

        if key is None:
            # print warning
            continue
        natoms = file["BENCHSETTINGS"]["BENCHATOMS"]

        tt = extract_rows(file, rows_to_extract)
        for row in rows_to_extract:
            data[row].append([natoms, *tt[key][row]])

    for row in rows_to_extract:
        data[row] = DataFrame(data[row], columns=["natoms", *TIMINGCOLS])
    return data
