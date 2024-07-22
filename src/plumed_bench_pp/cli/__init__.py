# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <iximiel@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

import plumed_bench_pp.utils as pbpputils

# import plumed_bench_pp.constants as plmdconst
from plumed_bench_pp.__about__ import __version__
from plumed_bench_pp.parser import parse_full_benchmark_output

# from plumed_bench_pp.plot import plot_histo
from plumed_bench_pp.tabulate import convert_to_table


def get_filelist(files:click.Path):
    filelist = []

    for f in files:
        with open(f) as ff:
            filelist.append(parse_full_benchmark_output(ff.readlines()))

    return filelist

def get_data(filelist,rows):
    data={}
    for k in pbpputils.get_kernels(filelist):
            data[k] = convert_to_table(filelist, rows, kernel=
            k, inputlist=".dat")
    return data


@click.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def kernels(files):
    """List the kernels in the given files"""
    filelist = get_filelist(files)


    for p in pbpputils.get_kernels(filelist):
        click.echo(p)


@click.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
@click.option("--output", "-o", type=click.STRING)
def plot(files, output):
    """Plot the data in the given files
    
    This assumes that the simulation data is given in kernels"""
    import matplotlib.pyplot as plt 
    # import matplotlib
    # matplotlib.use('Agg')
    from plumed_bench_pp.plot import plot_histo
    
    # click.echo(f"{files=}")
    # click.echo(f"{output=}")
    filelist = get_filelist(files)
    data = get_data(filelist, ["Plumed"])
    fig, ax=plt.subplots()
    plot_histo(ax,[data[k] for k in pbpputils.get_kernels(filelist)],"Plumed")

    if output is None:
        plt.show()
    else:
        fig.savefig(output)


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="plmdbpp")
def plmdbpp():
    pass


plmdbpp.add_command(kernels)
plmdbpp.add_command(plot)
