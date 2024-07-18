# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

import plumed_bench_pp.constants as pbppconst
import plumed_bench_pp.tabulate as pbpptbl


def the_test_extract_row(input_data):
    mydict, expectedcols = input_data
    retval = pbpptbl.extract_rows(mydict, rows=[pbppconst.CALCULATE, pbppconst.TOTALTIME])
    for key in expectedcols:
        assert pbppconst.CALCULATE in retval[key]
        assert expectedcols[key][pbppconst.CALCULATE] == retval[key][pbppconst.CALCULATE]

        assert pbppconst.TOTALTIME in retval[key]
        assert expectedcols[key][pbppconst.TOTALTIME] == retval[key][pbppconst.TOTALTIME]


def test_extract_row_2k1f(extracted_rows_output_2k1f):
    the_test_extract_row(extracted_rows_output_2k1f)


def test_extract_row_1k2f(extracted_rows_output_1k2f):
    the_test_extract_row(extracted_rows_output_1k2f)


def test_extract_row_noheader(extracted_rows_output_noheader):
    the_test_extract_row(extracted_rows_output_noheader)


def convert_to_table(filesdict, rows_to_extract, keylist):
    from pandas import DataFrame

    data = {}
    for row in rows_to_extract:
        data[row] = []
    for file, key in zip(filesdict, keylist):
        natoms = filesdict[file]["BENCHSETTINGS"]["BENCHATOMS"]
        tt = pbpptbl.extract_rows(filesdict[file], rows_to_extract)
        extracted_keys = tt.keys()
        if key in extracted_keys:
            for row in rows_to_extract:
                data[row].append([natoms, *tt[key][row]])
        # else:
        #     #warning?

    for row in rows_to_extract:
        data[row] = DataFrame(data[row], columns=["natoms", *pbppconst.TIMINGCOLS])
    return data


def test_get_table(incremental_output):
    for k in incremental_output:
        t = incremental_output[k]
        nat = t["BENCHSETTINGS"]["BENCHATOMS"]
        i = nat // 500
        dt = pbpptbl.extract_rows(t, rows=[pbppconst.TOTALTIME])
        assert dt[f"this+Coord{i}.dat"]["Plumed"][0] == 1
        assert dt[f"this+Coord{i}.dat"]["Plumed"][1] == 2 * i
    keylist = [f"this+Coord{i}.dat" for i in range(len(incremental_output))]
    mydict = convert_to_table(incremental_output, [pbppconst.CALCULATE, pbppconst.TOTALTIME], keylist)
    assert pbppconst.CALCULATE in mydict

    assert pbppconst.TOTALTIME in mydict
    assert mydict[pbppconst.TOTALTIME].Cycles == [1] * len(incremental_output)
