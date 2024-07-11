# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

from plumed_bench_pp.parser import parse_benchmark_output, parse_full_benchmark_output, parse_plumed_time_report


def test_parse_benchmark_output(readme_example_benchmark_output):
    example, expected = readme_example_benchmark_output
    lines = example.split("\n")
    assert parse_benchmark_output(lines) == expected


def test_parse_plumed_time_report(plumed_time_report):
    example, expected = plumed_time_report
    # this is an output of plumed with "DEBUG DETAILED_TIMERS" set
    lines = example.split("\n")
    assert parse_plumed_time_report(lines) == expected


def test_parse_full_benchmark_output(full_benchmark_output):
    example, expected = full_benchmark_output
    lines = example.split("\n")
    assert parse_full_benchmark_output(lines) == expected
