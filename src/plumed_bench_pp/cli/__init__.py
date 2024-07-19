# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <iximiel@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

# import plumed_bench_pp.constants as plmdconst
from plumed_bench_pp.__about__ import __version__

# from plumed_bench_pp.parser import parse_full_benchmark_output
# from plumed_bench_pp.plot import plot_histo
# from plumed_bench_pp.tabulate import convert_to_table


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="plmdbpp")
def plmdbpp():
    click.echo("Hello world!")
