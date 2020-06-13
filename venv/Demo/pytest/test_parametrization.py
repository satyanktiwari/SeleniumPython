import pytest

def sum(a,b):
    return a+b
@pytest.mark.parametrize("input1,input2,output",
                         [
                             (2,3,5),
                             (-1,-1,-2),
                             (-2,3,1)
                         ])
def test_calc_sum_1(input1,input2,output):
    result = sum(input1,input2)
    assert result == output

# def test_calc_sum_2():
#     result = sum(-1,-1)
#     assert result == -2
#
# def test_calc_sum_3():
#     result = sum(-2,3)
#     assert result == 1