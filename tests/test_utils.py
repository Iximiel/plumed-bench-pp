# SPDX-FileCopyrightText: 2024-present Daniele Rapetti <daniele.rapetti@sissa.it>
#
# SPDX-License-Identifier: MIT

from plumed_bench_pp.utils import kernel_name,get_kernels


def test_kernel_name():
    mydict = {}
    mydict[kernel_name(mydict, "bar")] = "bar->1"
    mydict[kernel_name(mydict, "bar")] = "bar->0"
    mydict[kernel_name(mydict, "foo")] = "foo->1"
    mydict[kernel_name(mydict, "foo")] = "foo->2"
    mydict[kernel_name(mydict, "foo")] = "foo->3"

    assert "foo" in mydict
    assert mydict["foo"] == "foo->1"
    assert "foo(1)" in mydict
    assert mydict["foo(1)"] == "foo->2"
    assert "foo(2)" in mydict
    assert mydict["foo(2)"] == "foo->3"

    assert "bar" in mydict
    assert mydict["bar"] == "bar->1"
    assert "bar(1)" in mydict
    assert mydict["bar(1)"] == "bar->0"

def test_get_kernels(incremental_output):
    parsed_input, _, _ = incremental_output 
    for k in parsed_input:
        ret=get_kernels(parsed_input[k])
        assert "this" in ret
        assert "that" in ret
def test_get_kernels_dict(incremental_output):
    parsed_input, _, _ = incremental_output
    ret=get_kernels(parsed_input)
    assert "this" in ret
    assert "that" in ret

def test_get_kernels_list(incremental_output):
    parsed_input, _, _ = incremental_output
    ret=get_kernels([parsed_input[k] for k in parsed_input])
    assert "this" in ret
    assert "that" in ret