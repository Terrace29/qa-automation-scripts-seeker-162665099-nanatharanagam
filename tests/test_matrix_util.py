from matrix_util import matrix_to_list

def test_matrix_basic():
    expected = [
        [1,2,3,4],
        [2,4,6,8],
        [3,6,9,12],
        [4,8,12,16]
    ]

    assert matrix_to_list(1,4) == expected