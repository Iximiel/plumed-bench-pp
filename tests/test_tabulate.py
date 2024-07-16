# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

import plumed_bench_pp.constants as pbppconst
import plumed_bench_pp.tabulate as pbpptbl

"4 Calculating (forward loop)"


def the_test_extract_row(input_data):
    mydict, expectedcols = input_data
    retval = pbpptbl.extract_row(mydict, rows=[pbppconst.CALCULATE, pbppconst.TOTALTIME])
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
