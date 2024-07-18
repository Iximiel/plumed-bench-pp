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


def test_check_file(incremental_output):
    # check file from list
    _, _, filelist = incremental_output
    # so that fname is in list
    fname = filelist[0]
    assert pbpptbl.checkfile(fname, filelist)

    # check for a pattern
    fname = filelist[0]
    assert pbpptbl.checkfile(fname, fname[:5])
    from re import compile

    # use a regex
    pattern = compile(r"Coord\d+\.dat")
    assert pbpptbl.checkfile(fname, pattern)


def test_convert_to_table(incremental_output):
    parsed_input, _, filelist = incremental_output
    mydict = pbpptbl.convert_to_table(
        parsed_input, [pbppconst.CALCULATE, pbppconst.TOTALTIME], kernel="this", inputlist=filelist
    )
    assert pbppconst.CALCULATE in mydict
    assert all(mydict[pbppconst.CALCULATE].Cycles == ([100] * (len(parsed_input))))
    assert all(mydict[pbppconst.CALCULATE].Total == [1.5 * i for i in range(1, 1 + len(parsed_input))])

    assert pbppconst.TOTALTIME in mydict
    assert all(mydict[pbppconst.TOTALTIME].Cycles == ([1] * (len(parsed_input))))
    assert all(mydict[pbppconst.TOTALTIME].Total == [2.0 * i for i in range(1, 1 + len(parsed_input))])

    mydict = pbpptbl.convert_to_table(
        parsed_input, [pbppconst.CALCULATE, pbppconst.TOTALTIME], kernel="that", inputlist=filelist
    )
    assert pbppconst.CALCULATE in mydict
    assert all(mydict[pbppconst.CALCULATE].Cycles == ([100] * (len(parsed_input))))
    assert all(mydict[pbppconst.CALCULATE].Total == [3.5 * i for i in range(1, 1 + len(parsed_input))])

    assert pbppconst.TOTALTIME in mydict
    assert all(mydict[pbppconst.TOTALTIME].Cycles == ([1] * (len(parsed_input))))
    assert all(mydict[pbppconst.TOTALTIME].Total == [4.0 * i for i in range(1, 1 + len(parsed_input))])
