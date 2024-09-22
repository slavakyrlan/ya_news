# test_pdb.py
import pytest


def transform_list(x):
    x.append(1)
    x.extend([2, 3])
    return x


def test_list():
    a = []
    a = transform_list(a)
    a = [4] + a
    a = sorted(a)
    assert a == [1, 2, 3, 4]


def cartesian_product(a, b):
    return a * b


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None

