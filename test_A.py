from collections import deque

from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

from pydantic import BaseModel


class Model(BaseModel):
    simple_list: list = None
    list_of_ints: List[int] = None

    simple_tuple: tuple = None
    tuple_of_different_types: Tuple[int, float, str, bool] = None

    simple_dict: dict = None
    dict_str_float: Dict[str, float] = None

    simple_set: set = None
    set_bytes: Set[bytes] = None
    frozen_set: FrozenSet[int] = None

    simple_bool: bool = None

    str_or_bytes: Union[str, bytes] = None
    none_or_str: Optional[str] = None

    sequence_of_ints: Sequence[int] = None

    compound: Dict[Union[str, bytes], List[Set[int]]] = None

    deque: Deque[int] = None


def test_A():

    assert ['1','2','3'] == Model(simple_list=['1', '2', '3']).simple_list
    assert [1,2,3] == Model(list_of_ints=['1', '2', '3']).list_of_ints

    assert {'a': 1, b'b': 2} == Model(simple_dict={'a': 1, b'b': 2}).simple_dict

    assert {'a': 1.0, 'b': 2.0} == Model(dict_str_float={'a': 1, b'b': 2}).dict_str_float

    assert (1, 2, 3, 4) == Model(simple_tuple=[1, 2, 3, 4]).simple_tuple

    assert (4, 3.0, '2', True) == Model(tuple_of_different_types=[4, 3, 2, 1]).tuple_of_different_types

    assert [1, 2, 3, 4] == Model(sequence_of_ints=[1, 2, 3, 4]).sequence_of_ints

    assert (1, 2, 3, 4) == Model(sequence_of_ints=(1, 2, 3, 4)).sequence_of_ints

    assert deque([1, 2, 3]) == Model(deque=[1, 2, 3]).deque

    assert Model(simple_bool=True).simple_bool
    assert not Model(simple_bool=False).simple_bool
