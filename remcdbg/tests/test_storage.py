from __future__ import print_function
from remcdbg.storage import choose_storage
from hypothesis import given
import hypothesis.strategies as st
POSSIBLE_STORAGES = [{'dict': None}, {'berkeleydb': {'filename': './db'}},
                     {"redis": [('localhost', 6379)]}]  # ,
#                     {'rocksdb': {'filename': '.rdb'}}]


@given(s=st.sampled_from(POSSIBLE_STORAGES), k=st.binary(), v=st.binary())
def tests_setget_string(s, k, v):
    s = choose_storage(s)
    s[k] = v
    assert s[k] == v
