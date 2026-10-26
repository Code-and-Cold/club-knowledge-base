import pytest

from main import binary_search as search


@pytest.mark.parametrize("array,target,expected", [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12,34,234,512], 512, 8),
    ([-1,0,3,5,9,12,34,234,512], -1, 0),
    ([-123,-50,-10,-1,3,5,9,12,34], -10, 2),
    ([-10000, -10, 10, 10000], -10, 1),
    ([-10000, -10, 10, 10000], -11, -1),
    ([-123,-50,-10,-1,3,5,9,12,34], -49, -1),
    ([-1,0,3,5,9], 2, -1),
])
def test_search(array, target, expected):

    assert search(array, target) == expected
