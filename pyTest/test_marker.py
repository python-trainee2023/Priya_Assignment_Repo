import pytest
def func(x):
    return x*2

def test_method():
    assert func(3) == 8

@pytest.mark.xfail
def test_method2():
    assert func(3) ==9

@pytest.mark.skip
def test_method3():
    assert func(3) == 9

@pytest.mark.focus
def test_method3()