# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

import re
from itertools import dropwhile

# using raw string (r) to avoid warnings with the escaped characters
__FLOATMATCH = r"[+-]?(?:\d+(?:[.]\d*)?(?:e[+-]?\d+)?|[.]\d+(?:e[+-]?\d+)?)"
__Kernel = re.compile(r"Kernel:\s*(\S*)")
__Input = re.compile(r"Input:\s*(\S*)")
__Comparative = re.compile(rf"Comparative:\s*({__FLOATMATCH}) \+\- ({__FLOATMATCH})")
__Data = re.compile(
    rf"(?:PLUMED: |BENCH:  )(?P<name>.+)\s+(?P<Cycles>[0-9]+)+\s+"
    rf"(?P<Total>{__FLOATMATCH})+\s+"
    rf"(?P<Average>{__FLOATMATCH})+\s+"
    rf"(?P<Minimum>{__FLOATMATCH})+\s+"
    rf"(?P<Maximum>{__FLOATMATCH})+"
)


def parse_benchmark_output(lines: list[str]) -> dict:
    """
    Parses the benchmark output lines to extract kernel information and performance statistics.

    Args:
        lines (list[str]): The list of lines containing benchmark output data.

    Returns:
        dict: A dictionary containing the parsed benchmark data.
    """
    data = {}
    kernel = {}
    for line in lines:
        if result := __Kernel.search(line):
            if len(kernel) > 0:
                data[kernel["kernel"]] = kernel
                kernel = {}
            kernel["kernel"] = result.group(1)
        elif result := __Input.search(line):
            kernel["input"] = result.group(1)
        elif result := __Comparative.search(line):
            kernel["compare"] = {
                "fraction": float(result.group(1)),
                "error": float(result.group(2)),
            }
        elif result := __Data.search(line):
            name = result.group("name").strip()
            if name == "":
                name = "Plumed"
            kernel[name] = {
                "Cycles": int(result.group("Cycles")),
                "Total": float(result.group("Total")),
                "Average": float(result.group("Average")),
                "Minimum": float(result.group("Minimum")),
                "Maximum": float(result.group("Maximum")),
            }
    # add the last kernel
    if len(kernel) > 0:
        data[kernel["kernel"]] = kernel
    return data


def parse_plumed_time_report(lines: list[str]) -> dict:
    data = {}
    for line in lines:
        if result := __Data.search(line):
            name = result.group("name").strip()
            if name == "":
                name = "Plumed"
            data[name] = {
                "Cycles": int(result.group("Cycles")),
                "Total": float(result.group("Total")),
                "Average": float(result.group("Average")),
                "Minimum": float(result.group("Minimum")),
                "Maximum": float(result.group("Maximum")),
            }
    return data


def parse_full_benchmark_output(lines: list[str]) -> dict:
    # more or less the output for the times is few lines after the message for the MD starting
    parsing_lines = dropwhile(lambda line: not line.startswith("BENCH:  Starting MD loop"), lines)

    return parse_benchmark_output(parsing_lines)
