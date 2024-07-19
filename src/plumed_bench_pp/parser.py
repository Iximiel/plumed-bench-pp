# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

import re
from dataclasses import dataclass
from itertools import dropwhile
from typing import TYPE_CHECKING

from plumed_bench_pp.utils import kernel_name

if TYPE_CHECKING:
    from collections.abc import Iterable

# using raw string (r) to avoid warnings with the escaped characters
__FLOATMATCH = r"[+-]?(?:\d+(?:[.]\d*)?(?:e[+-]?\d+)?|[.]\d+(?:e[+-]?\d+)?)"
__Kernel = re.compile(r"Kernel:\s*(\S*)")
__Input = re.compile(r"Input:\s*(\S*)")
__Comparative = re.compile(rf"Comparative:\s*({__FLOATMATCH}) \+\- ({__FLOATMATCH})")
# __NumerOfAtoms = re.compile(r" Number of atoms: (\d+)")
__Data = re.compile(
    rf"(?:PLUMED: |BENCH:  )(?P<name>.+)\s+(?P<Cycles>[0-9]+)+\s+"
    rf"(?P<Total>{__FLOATMATCH})+\s+"
    rf"(?P<Average>{__FLOATMATCH})+\s+"
    rf"(?P<Minimum>{__FLOATMATCH})+\s+"
    rf"(?P<Maximum>{__FLOATMATCH})+"
)
# these are the regexes for the first few lines of the benchmark output
# BENCH:  Welcome to PLUMED benchmark
__BMKernelList = re.compile(r"BENCH:  Using --kernel=(.+)")
__BMPlumedList = re.compile(r"BENCH:  Using --plumed=(.+)")
__BMSteps = re.compile(r"BENCH:  Using --nsteps=(\d+)")
__BMNatoms = re.compile(r"BENCH:  Using --natoms=(\d+)")
__BMMaxtime = re.compile(r"BENCH:  Using --maxtime=({__FLOATMATCH}|[-+]?\d+)")
__BMSleep = re.compile(r"BENCH:  Using --sleep=(\d+)")
__BMAtomDistributions = re.compile(r"BENCH:  Using --atom-distribution=(.+)")
__BMIsSuffled = re.compile(r"BENCH:  Using --shuffled")
__BMUseDomainDecomposition = re.compile(r"BENCH:  Using --domain-decomposition")
# BENCH:  Initializing the setup of the kernel(s)


@dataclass
class BenchmarkRow:
    # name: str
    cycles: int
    total: float
    average: float
    minimum: float
    maximum: float

    def as_list(self) -> list:
        return [self.cycles, self.total, self.average, self.minimum, self.maximum]

    @staticmethod
    def from_re_match(result: re.Match) -> "BenchmarkRow":
        """
        A method to create a BenchmarkRow instance from a regex match result.

        Args:
            result (re.Match): The regex match result containing the required groups.

        Returns:
            BenchmarkRow: A BenchmarkRow instance initialized with the extracted data.
        """
        return BenchmarkRow(
            cycles=int(result.group("Cycles")),
            total=float(result.group("Total")),
            average=float(result.group("Average")),
            minimum=float(result.group("Minimum")),
            maximum=float(result.group("Maximum")),
        )

    @staticmethod
    def from_dict(data: dict) -> "BenchmarkRow":
        """
        Creates a new instance of the BenchmarkRow class from a dictionary containing the necessary data.

        Args:
            data (dict): A dictionary with the following keys: "Cycles", "Total", "Average", "Minimum", and "Maximum".

        Returns:
            BenchmarkRow: A new instance of the BenchmarkRow class initialized with the data from the dictionary.
        """

        return BenchmarkRow(
            cycles=data["Cycles"],
            total=data["Total"],
            average=data["Average"],
            minimum=data["Minimum"],
            maximum=data["Maximum"],
        )


@dataclass
class KernelBenchmark:
    kernel: str
    input: str
    compare: dict
    rows: dict

    @staticmethod
    def empty() -> "KernelBenchmark":
        return KernelBenchmark("", "", {}, {})

    def has_data(self) -> bool:
        return len(self.rows) > 0 or len(self.compare) > 0 or self.input != "" or self.kernel != ""


def parse_benchmark_output(lines: "list[str] | Iterable[str]") -> dict:
    """
    Parses the benchmark output lines to extract kernel information and performance statistics.

    Args:
        lines (list[str]): The list of lines containing benchmark output data.

    Returns:
        dict: A dictionary containing the parsed benchmark data.
    """
    data: dict = {}
    kernel: KernelBenchmark = KernelBenchmark.empty()
    for line in lines:
        if result := __Kernel.search(line):
            if kernel.has_data():
                data[kernel_name(data, f"{kernel.kernel}+{kernel.input}")] = kernel

                kernel = KernelBenchmark.empty()
            kernel.kernel = result.group(1)
        elif result := __Input.search(line):
            kernel.input = result.group(1)
        elif result := __Comparative.search(line):
            kernel.compare = {
                "fraction": float(result.group(1)),
                "error": float(result.group(2)),
            }
        elif result := __Data.search(line):
            name = result.group("name").strip()
            if name == "":
                name = "Plumed"
            kernel.rows[name] = BenchmarkRow.from_re_match(result)
    # add the last kernel
    if kernel.has_data():
        data[kernel_name(data, f"{kernel.kernel}+{kernel.input}")] = kernel
    return data


def parse_plumed_time_report(lines: list[str]) -> KernelBenchmark:
    data: KernelBenchmark = KernelBenchmark.empty()
    for line in lines:
        if result := __Data.search(line):
            name = result.group("name").strip()
            if name == "":
                name = "Plumed"
            data.rows[name] = BenchmarkRow.from_re_match(result)
    return data


def parse_full_benchmark_output(lines: list[str]) -> dict:
    # more or less the output for the times is few lines after the message for the MD starting

    header = {}
    if "BENCH:  Welcome to PLUMED benchmark" in lines[0]:
        # there is an header :)
        for line in lines:
            if "BENCH:  Initializing the setup of the kernel(s)" in line:
                break
            if result := __BMKernelList.search(line):
                header["BENCHKERNELS"] = result.group(1).split(":")
            elif result := __BMPlumedList.search(line):
                header["BENCHINPUTS"] = result.group(1).split(":")
            elif result := __BMSteps.search(line):
                header["BENCHEXPECTEDSTEPS"] = int(result.group(1))
            elif result := __BMNatoms.search(line):
                header["BENCHATOMS"] = int(result.group(1))
            elif result := __BMMaxtime.search(line):
                header["BENCHMAXTIME"] = float(result.group(1))
            elif result := __BMSleep.search(line):
                header["BENCHSLEEP"] = float(result.group(1))
            elif result := __BMAtomDistributions.search(line):
                header["BENCHATOMDISTRIBUTION"] = result.group(1)
            elif result := __BMIsSuffled.search(line):
                header["BENCHSHUFFLED"] = True
            elif result := __BMUseDomainDecomposition.search(line):
                header["BENCHDOMAINDECOMPOSITION"] = True

    parsing_lines = dropwhile(lambda line: not line.startswith("BENCH:  Starting MD loop"), lines)
    results = parse_benchmark_output(parsing_lines)
    if len(header) > 0:
        results["BENCHSETTINGS"] = header
    return results
